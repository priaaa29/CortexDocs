import streamlit as st


def inject_css() -> None:
    st.markdown("<style>/* styles coming soon */</style>", unsafe_allow_html=True)
