import os
import json
from typing import Generator

from groq import Groq
from flashrank import Ranker, RerankRequest

from src.config import (
    GROQ_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS,
    HISTORY_WINDOW, RERANK_MODEL_NAME, RERANK_TOP_K,
)


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


# ── Streaming answer ───────────────────────────────────────────────────────────

def build_context(retrieved_chunks: list[dict]) -> str:
    return "\n\n".join(
        f"Source [{i+1}]: {r['doc_name']} (Page {r.get('page', 'N/A')})\n{r['text']}"
        for i, r in enumerate(retrieved_chunks)
    )


def stream_answer(query: str, retrieved_chunks: list[dict], history: list[dict], query_type: str) -> Generator[str, None, None]:
    """Yield streamed tokens from Groq."""
    context = build_context(retrieved_chunks)

    system_prompt = f"""You are CortexDocs — a precise Document Intelligence Assistant.
Query type: {query_type.upper()}

Structure your answer:
- Opening summary sentence
- Key bullet points with details
- Cite sources as [1], [2] …

Use only the provided context. Do not fabricate information."""

    messages = [{"role": "system", "content": system_prompt}]
    for msg in history[-HISTORY_WINDOW:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"})

    client = _groq_client()
    stream = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS,
        stream=True,
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
