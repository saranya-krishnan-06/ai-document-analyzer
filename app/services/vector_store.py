# app/services/vector_store.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.core.logger import logger

# Load embedding model once — shared across the app
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
logger.info("Embedding model loaded: all-MiniLM-L6-v2")

DIMENSION = 384

# In-memory store — resets on restart
documents: list[str] = []
index: faiss.IndexFlatL2 | None = None


def add_documents(chunks: list[str]) -> None:
    """Embed chunks and add them to the FAISS index."""
    global documents, index

    if not chunks:
        return

    vectors = embedding_model.encode(chunks)
    vectors = np.array(vectors, dtype="float32")

    if index is None:
        index = faiss.IndexFlatL2(DIMENSION)

    index.add(vectors)
    documents.extend(chunks)
    logger.info(f"Added {len(chunks)} chunks. Total: {len(documents)}")


def search(query: str, k: int = 3) -> list[str]:
    """Return the k most relevant chunks for a query."""
    if index is None or len(documents) == 0:
        logger.warning("Search called but no documents have been added yet.")
        return []

    query_vector = embedding_model.encode([query])
    query_vector = np.array(query_vector, dtype="float32")

    k = min(k, len(documents))  # can't fetch more than we have
    distances, indices = index.search(query_vector, k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(documents):
            results.append(documents[i])

    return results