import streamlit as st
from dotenv import load_dotenv

load_dotenv()

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

inject_css()

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

if st.session_state.index is None and not st.session_state.chunks:
    with st.spinner("Loading index…"):
        idx, chunks, bm25, model = load_index(DATA_DIR)
    if idx is not None:
        st.session_state.index = idx
        st.session_state.chunks = chunks
        st.session_state.bm25 = bm25
        st.session_state.embedding_model = model

render_sidebar()
render_chat()
