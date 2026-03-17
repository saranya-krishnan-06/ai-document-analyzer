import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
embeddings = None
index = None


def add_documents(chunks):

    global documents, embeddings, index

    vectors = model.encode(chunks)

    documents.extend(chunks)

    if embeddings is None:
        embeddings = vectors
    else:
        embeddings = np.vstack((embeddings, vectors))

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)


def search(query):

    global index

    query_vector = model.encode([query])

    distances, indices = index.search(query_vector, k=3)

    results = []

    for i in indices[0]:
        results.append(documents[i])

    return results