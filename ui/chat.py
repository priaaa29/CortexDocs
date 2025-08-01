import streamlit as st

from src.retrieval import retrieve
from src.llm import classify_query, rerank, stream_answer


def render_chat() -> None:
    """Render the main chat area: history + input."""
    if not st.session_state.get("chunks"):
        st.markdown(
            """
            <div class="empty-state">
                <div class="label">Ready</div>
                <h2>No documents indexed</h2>
                <p>Upload PDF or TXT files from the sidebar to get started.</p>
                <div class="hint">Drop files in the sidebar to begin</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.stop()

    for msg in st.session_state.get("messages", []):
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask anything about your documents…"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        _generate_response(prompt)
