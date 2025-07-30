import streamlit as st

from src.document_processor import process_pdf, process_txt
from src.retrieval import add_chunks, save_index
from src.config import INDEX_PATH, METADATA_PATH


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("### CortexDocs")
        st.divider()

        uploaded_files = st.file_uploader(
            "Upload PDF or TXT files",
            type=["pdf", "txt"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            if st.button("Process & Index", type="primary", use_container_width=True):
                _process_uploads(uploaded_files)


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
    st.success(f"{len(new_chunks)} chunks indexed.")
    st.rerun()
