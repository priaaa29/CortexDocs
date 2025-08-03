import streamlit as st

from src.retrieval import retrieve
from src.llm import classify_query, rerank, stream_answer

_BADGE = {
    "factual":    ("badge-factual",    "Factual"),
    "summary":    ("badge-summary",    "Summary"),
    "comparison": ("badge-comparison", "Comparison"),
    "other":      ("badge-other",      "General"),
}


def render_chat() -> None:
    """Render the main chat area: history + input."""
    if not st.session_state.get("chunks"):
        st.markdown(
            """
            <div class="empty-state">
                <div class="label">Ready</div>
                <div class="rule"></div>
                <h2>No documents indexed</h2>
                <p>Upload PDF or TXT files from the sidebar. CortexDocs will chunk,
                embed, and index them instantly — then answer questions with full
                source citations.</p>
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


def _generate_response(prompt: str) -> None:
    with st.chat_message("assistant"):
        with st.spinner("Analysing query…"):
            classification = classify_query(prompt)
            q_type = classification.get("type", "factual")

        badge_class, badge_label = _BADGE.get(q_type, _BADGE["other"])
        st.markdown(
            f'<span class="query-badge {badge_class}">{badge_label}</span>',
            unsafe_allow_html=True,
        )

        with st.spinner("Retrieving relevant context…"):
            filter_docs = None
            selected = st.session_state.get("selected_docs", ["All"])
            if "All" not in selected:
                filter_docs = set(selected)
            fused = retrieve(
                prompt,
                st.session_state.index,
                st.session_state.chunks,
                st.session_state.bm25,
                st.session_state.embedding_model,
                q_type,
                filter_docs=filter_docs,
            )
            top_chunks = rerank(prompt, fused)

        placeholder = st.empty()
        full_response = ""
        for token in stream_answer(prompt, top_chunks, st.session_state.get("messages", []), q_type):
            full_response += token
            placeholder.markdown(full_response + "▌")
        placeholder.markdown(full_response)

        _render_sources(top_chunks)

    st.session_state.messages.append({"role": "assistant", "content": full_response})


def _render_sources(chunks: list[dict]) -> None:
    if not chunks:
        return
    st.markdown('<div class="sources-header">Sources</div>', unsafe_allow_html=True)
    for i, chunk in enumerate(chunks, 1):
        with st.expander(f"[{i}]  {chunk['doc_name']}  —  p.{chunk.get('page', 'N/A')}"):
            st.markdown(
                f"<div class='source-body'>{chunk['text']}</div>",
                unsafe_allow_html=True,
            )
