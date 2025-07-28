import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="CortexDocs",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("CortexDocs")
st.write("Document Intelligence Assistant — work in progress")
