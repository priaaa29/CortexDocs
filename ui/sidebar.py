import os
import streamlit as st

from src.document_processor import process_pdf, process_txt
from src.retrieval import add_chunks, save_index
from src.config import INDEX_PATH, METADATA_PATH


def render_sidebar() -> None:
    """Render the full sidebar: branding, upload, stats, filter, clear."""
    with st.sidebar:
        # ── Brand ──────────────────────────────────────────────────────────────
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="wordmark">Cortex<em>Docs</em></div>
                <div class="tagline">Document Intelligence</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Stats ───────────────────────────────────────────────────────────────
        chunk_count = len(st.session_state.get("chunks", []))
        doc_names = {c["doc_name"] for c in st.session_state.get("chunks", [])}
        doc_count = len(doc_names)

        st.markdown(
            f"""
            <div class="stat-row">
                <div class="stat-card">
                    <div class="stat-value">{doc_count}</div>
                    <div class="stat-label">Documents</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{chunk_count}</div>
                    <div class="stat-label">Chunks</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # ── Upload ──────────────────────────────────────────────────────────────
        st.markdown('<div class="sidebar-section-label">Upload</div>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "PDF or TXT files",
            type=["pdf", "txt"],
            accept_multiple_files=True,
            label_visibility="collapsed",
        )

        if uploaded_files:
            if st.button("Process & Index", type="primary", use_container_width=True):
                _process_uploads(uploaded_files)

        st.divider()

        # ── Document filter ─────────────────────────────────────────────────────
        if chunk_count > 0:
            st.markdown('<div class="sidebar-section-label">Filter</div>', unsafe_allow_html=True)
            all_docs = sorted(doc_names)
            selected = st.multiselect(
                "Active documents",
                ["All"] + all_docs,
                default=st.session_state.get("selected_docs", ["All"]),
                label_visibility="collapsed",
            )
            st.session_state.selected_docs = selected
            st.divider()

            if st.button("Clear All Data", use_container_width=True):
                _clear_all()

        # ── Footer ──────────────────────────────────────────────────────────────
        st.markdown(
            "<div class='sidebar-footer'>Hybrid RAG · RRF · FlashRank</div>",
            unsafe_allow_html=True,
        )


def _process_uploads(uploaded_files) -> None:
    progress = st.progress(0, text="Extracting text…")
    new_chunks = []
    for i, file in enumerate(uploaded_files):
        progress.progress((i + 1) / len(uploaded_files), text=f"Processing {file.name}…")
        if file.type == "application/pdf":
            new_chunks.extend(process_pdf(file))
        else:
            new_chunks.extend(process_txt(file))
    if not new_chunks:
        st.error("No text could be extracted from the uploaded files.")
        return
    progress.progress(0.8, text="Building index…")
    index, all_chunks, bm25, model = add_chunks(
        new_chunks,
        st.session_state.get("chunks", []),
        st.session_state.get("index"),
        st.session_state.get("embedding_model"),
    )
    progress.progress(0.95, text="Saving to disk…")
    save_index(index, all_chunks)
    st.session_state.index = index
    st.session_state.chunks = all_chunks
    st.session_state.bm25 = bm25
    st.session_state.embedding_model = model
    progress.progress(1.0, text="Done!")
    st.success(f"{len(new_chunks)} chunks indexed across {len(uploaded_files)} file(s).")
    st.rerun()


def _clear_all() -> None:
    for path in [INDEX_PATH, METADATA_PATH]:
        if os.path.exists(path):
            os.remove(path)
    for key in ["index", "embedding_model", "bm25"]:
        st.session_state[key] = None
    st.session_state.chunks = []
    st.session_state.messages = []
    st.session_state.selected_docs = ["All"]
    st.rerun()
