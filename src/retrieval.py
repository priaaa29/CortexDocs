import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from src.config import EMBEDDING_MODEL_NAME
from src.document_processor import tokenize


def _build_bm25(chunks: list[dict]) -> BM25Okapi:
    tokenized = [tokenize(c["text"]) for c in chunks]
    return BM25Okapi(tokenized)


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
