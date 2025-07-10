import os

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
INDEX_PATH = os.path.join(DATA_DIR, "faiss_index.bin")
METADATA_PATH = os.path.join(DATA_DIR, "metadata.json")

# ── Models ─────────────────────────────────────────────────────────────────────
GROQ_MODEL = "llama-3.3-70b-versatile"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
RERANK_MODEL_NAME = "ms-marco-MiniLM-L-12-v2"

# ── Chunking ───────────────────────────────────────────────────────────────────
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200

# ── Retrieval ──────────────────────────────────────────────────────────────────
VECTOR_WEIGHT = 0.6
BM25_WEIGHT = 0.4
RRF_K = 20          # Lower values favour top-ranked results more
BASE_K_FACTUAL = 15
BASE_K_SUMMARY = 25
FUSION_TOP_N = 18
RERANK_TOP_K = 7

# ── LLM ────────────────────────────────────────────────────────────────────────
LLM_TEMPERATURE = 0.3
LLM_MAX_TOKENS = 1200
HISTORY_WINDOW = 6  # how many prior turns to pass to the LLM
