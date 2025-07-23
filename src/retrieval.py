import os
import json
from collections import defaultdict

import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from src.config import (
    INDEX_PATH, METADATA_PATH, EMBEDDING_MODEL_NAME,
    VECTOR_WEIGHT, BM25_WEIGHT, RRF_K,
    BASE_K_FACTUAL, BASE_K_SUMMARY, FUSION_TOP_N,
)
from src.document_processor import tokenize


# ── Persistence ────────────────────────────────────────────────────────────────

def load_index(data_dir: str) -> tuple:
    """Load persisted FAISS index, chunks, and rebuild BM25. Returns (index, chunks, bm25, model) or (None, [], None, None)."""
    if not (os.path.exists(INDEX_PATH) and os.path.exists(METADATA_PATH)):
        return None, [], None, None

    try:
        index = faiss.read_index(INDEX_PATH)
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        chunks = data.get("chunks", [])
        model = SentenceTransformer(EMBEDDING_MODEL_NAME)
        bm25 = _build_bm25(chunks) if chunks else None
        return index, chunks, bm25, model
    except Exception:
        return None, [], None, None


def save_index(index, chunks: list[dict]) -> None:
    """Persist FAISS index and chunk metadata to disk."""
    os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
    faiss.write_index(index, INDEX_PATH)
    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks}, f, ensure_ascii=False, indent=2)


# ── Index building ─────────────────────────────────────────────────────────────

def _build_bm25(chunks: list[dict]) -> BM25Okapi:
    tokenized = [tokenize(c["text"]) for c in chunks]
    return BM25Okapi(tokenized)


def add_chunks(new_chunks: list[dict], existing_chunks: list[dict], existing_index, model=None):
    """Embed new chunks, add to FAISS index, rebuild BM25. Returns (index, all_chunks, bm25, model)."""
    if model is None:
        model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    texts = [c["text"] for c in new_chunks]
    embeddings = model.encode(texts, normalize_embeddings=True).astype("float32")

    if existing_index is None:
        dim = embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)
    else:
        index = existing_index

    index.add(embeddings)
    all_chunks = existing_chunks + new_chunks
    bm25 = _build_bm25(all_chunks)
    return index, all_chunks, bm25, model


# ── Search ─────────────────────────────────────────────────────────────────────

def vector_search(query: str, index, chunks: list[dict], model, k: int):
    q_emb = model.encode([query], normalize_embeddings=True).astype("float32")
    distances, indices = index.search(q_emb, k)
    results = [chunks[i] for i in indices[0] if i < len(chunks)]
    scores = distances[0].tolist()
    return results, scores


def bm25_search(query: str, bm25: BM25Okapi, chunks: list[dict], k: int):
    tokens = tokenize(query)
    all_scores = bm25.get_scores(tokens)
    top_indices = np.argsort(all_scores)[::-1][:k]
    results = [chunks[i] for i in top_indices]
    scores = [all_scores[i] for i in top_indices]
    return results, scores


def hybrid_score_fusion(
    vector_results, bm25_results,
    vector_scores, bm25_scores,
    all_chunks: list[dict],
    top_n: int = FUSION_TOP_N,
) -> list[dict]:
    """Combine vector and BM25 results using RRF + weighted normalised scores."""
    score_dict: dict[int, float] = defaultdict(float)
    rank_dict: dict[int, dict] = defaultdict(
        lambda: {"vector_rank": float("inf"), "bm25_rank": float("inf")}
    )

    for rank, (chunk, score) in enumerate(zip(vector_results, vector_scores), 1):
        idx = id(chunk)
        rank_dict[idx]["vector_rank"] = rank
        score_dict[idx] += VECTOR_WEIGHT * score

    for rank, (chunk, score) in enumerate(zip(bm25_results, bm25_scores), 1):
        idx = id(chunk)
        rank_dict[idx]["bm25_rank"] = rank
        score_dict[idx] += BM25_WEIGHT * score

    for idx, ranks in rank_dict.items():
        rrf = 0.0
        if ranks["vector_rank"] < float("inf"):
            rrf += 1.0 / (RRF_K + ranks["vector_rank"])
        if ranks["bm25_rank"] < float("inf"):
            rrf += 1.0 / (RRF_K + ranks["bm25_rank"])
        score_dict[idx] += rrf * 10

    sorted_items = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:top_n]
    id_to_chunk = {id(c): c for c in all_chunks}
    return [id_to_chunk[idx] for idx, _ in sorted_items if idx in id_to_chunk]


def retrieve(query: str, index, chunks: list[dict], bm25, model, query_type: str, filter_docs=None) -> list[dict]:
    """Full retrieval pipeline: vector + BM25 -> fusion -> optional doc filter."""
    k = BASE_K_SUMMARY if query_type in ("summary", "comparison") else BASE_K_FACTUAL

    v_results, v_scores = vector_search(query, index, chunks, model, k)
    b_results, b_scores = bm25_search(query, bm25, chunks, k)
    fused = hybrid_score_fusion(v_results, b_results, v_scores, b_scores, chunks)

    if filter_docs:
        fused = [c for c in fused if c["doc_name"] in filter_docs]

    return fused if fused else v_results[:10]
