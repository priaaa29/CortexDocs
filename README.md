# CortexDocs

A document intelligence assistant powered by hybrid RAG (Retrieval-Augmented Generation).

## Features
- Upload PDFs and TXT files
- Hybrid retrieval: FAISS vector search + BM25, fused with Reciprocal Rank Fusion
- Cross-encoder reranking via FlashRank
- Streaming answers with source citations, powered by Groq (llama-3.3-70b-versatile)
- Query classification: factual / summary / comparison / general
- Persistent index (survives app restarts)

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # add your GROQ_API_KEY
streamlit run app.py
```

## Architecture

```
app.py              # Streamlit entry point
src/
  config.py         # All tunable constants
  document_processor.py   # PDF/TXT parsing + chunking
  retrieval.py      # FAISS + BM25 + RRF fusion + persistence
  llm.py            # Groq client, query classification, reranking, streaming
ui/
  sidebar.py        # Upload, stats, filter, clear
  chat.py           # Chat history, response generation, source expanders
  styles.py         # CSS design system (JetBrains Mono + Instrument Serif)
data/               # Persisted FAISS index + metadata (gitignored)
```
