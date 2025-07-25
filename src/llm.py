import os
import json
from typing import Generator

from groq import Groq
from flashrank import Ranker, RerankRequest

from src.config import GROQ_MODEL, RERANK_MODEL_NAME, RERANK_TOP_K


def _groq_client() -> Groq:
    return Groq(api_key=os.getenv("GROQ_API_KEY"))


# ── Query classification ───────────────────────────────────────────────────────

def classify_query(query: str) -> dict:
    """Classify query as summary | factual | comparison | other."""
    try:
        client = _groq_client()
        prompt = (
            f'Classify query as: summary, factual, comparison, or other. '
            f'Return ONLY JSON {{"type": "...", "reason": "short"}} '
            f'Query: {query}'
        )
        resp = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=100,
        )
        return json.loads(resp.choices[0].message.content.strip())
    except Exception:
        return {"type": "factual", "reason": "fallback"}


# ── Reranking ──────────────────────────────────────────────────────────────────

def rerank(query: str, chunks: list[dict], top_k: int = RERANK_TOP_K) -> list[dict]:
    """Rerank chunks using FlashRank cross-encoder."""
    ranker = Ranker(model_name=RERANK_MODEL_NAME)
    passages = [{"text": c["text"], "id": i} for i, c in enumerate(chunks)]
    reranked = ranker.rerank(RerankRequest(query=query, passages=passages))
    return [chunks[r["id"]] for r in reranked[:top_k]]
