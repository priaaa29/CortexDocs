import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page config (must be first Streamlit call) ─────────────────────────────────
st.set_page_config(
    page_title="CortexDocs",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

from ui.styles import inject_css
from ui.sidebar import render_sidebar
from ui.chat import render_chat
from src.retrieval import load_index
from src.config import DATA_DIR

# ── Inject custom CSS ──────────────────────────────────────────────────────────
inject_css()

# ── Session state initialisation ──────────────────────────────────────────────
defaults = {
    "index": None,
    "chunks": [],
    "bm25": None,
    "embedding_model": None,
    "messages": [],
    "selected_docs": ["All"],
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ── Load persisted index on first run ─────────────────────────────────────────
if st.session_state.index is None and not st.session_state.chunks:
    with st.spinner("Loading index…"):
        idx, chunks, bm25, model = load_index(DATA_DIR)
    if idx is not None:
        st.session_state.index = idx
        st.session_state.chunks = chunks
        st.session_state.bm25 = bm25
        st.session_state.embedding_model = model

# ── Context bar (thin, functional — not branded) ──────────────────────────────
_chunk_count = len(st.session_state.get("chunks", []))
_doc_count   = len({c["doc_name"] for c in st.session_state.get("chunks", [])})
_active      = _doc_count > 0
_dot_class   = "cb-dot active" if _active else "cb-dot"
_status_text = f"{_doc_count} doc{'s' if _doc_count != 1 else ''} &nbsp;·&nbsp; {_chunk_count} chunks" if _active else "No documents indexed"

st.markdown(
    f"""
    <div class="context-bar">
        <span class="cb-model">llama-3.3-70b-versatile</span>
        <span class="cb-right">
            <span class="{_dot_class}"></span>
            <span class="cb-status">{_status_text}</span>
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Sidebar ────────────────────────────────────────────────────────────────────
render_sidebar()

# ── Main chat area ─────────────────────────────────────────────────────────────
render_chat()
