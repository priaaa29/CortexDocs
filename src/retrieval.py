import os
import json
import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from src.config import (
    INDEX_PATH, METADATA_PATH, EMBEDDING_MODEL_NAME,
)
from src.document_processor import tokenize


def _build_bm25(chunks: list[dict]) -> BM25Okapi:
    tokenized = [tokenize(c["text"]) for c in chunks]
    return BM25Okapi(tokenized)


def load_index(data_dir: str) -> tuple:
    """Load persisted FAISS index and rebuild BM25. Returns (index, chunks, bm25, model)."""
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


def add_chunks(new_chunks: list[dict], existing_chunks: list[dict], existing_index, model=None):
    """Embed new chunks, add to FAISS index, rebuild BM25."""
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
