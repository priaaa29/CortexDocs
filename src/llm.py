import os
import json

from groq import Groq

from src.config import GROQ_MODEL


def _groq_client() -> Groq:
    return Groq(api_key=os.getenv("GROQ_API_KEY"))


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
