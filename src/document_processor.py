import io
import re
from pypdf import PdfReader


CHUNK_SIZE = 800
CHUNK_OVERLAP = 200


def split_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap
    return chunks


def process_pdf(file) -> list[dict]:
    """Extract and chunk text from an uploaded PDF file."""
    reader = PdfReader(io.BytesIO(file.getvalue()))
    chunks = []
    for page_num, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if text.strip():
            for chunk_text in split_text(text):
                chunks.append({
                    "text": chunk_text,
                    "doc_name": file.name,
                    "page": page_num,
                })
    return chunks


def process_txt(file) -> list[dict]:
    """Extract and chunk text from an uploaded TXT file."""
    text = file.getvalue().decode("utf-8")
    return [
        {"text": chunk_text, "doc_name": file.name, "page": "N/A"}
        for chunk_text in split_text(text)
    ]


def tokenize(text: str) -> list[str]:
    """Simple word tokeniser used by BM25."""
    return re.findall(r'\w+', text.lower())
