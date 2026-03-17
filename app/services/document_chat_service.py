from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import faiss
import numpy as np

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# FAISS index
dimension = 384
index = faiss.IndexFlatL2(dimension)

# Store chunks
documents = []


def add_document_chunks(chunks):
    vectors = embedding_model.encode(chunks)
    index.add(np.array(vectors))

    for chunk in chunks:
        documents.append(chunk)


def search_similar_chunks(query, k=3):
    query_vector = embedding_model.encode([query])

    distances, indices = index.search(np.array(query_vector), k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")


def answer_question(question):
    chunks = search_similar_chunks(question)

    context = " ".join(chunks)

    prompt = f"""
Answer the question based on the context.

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(**inputs, max_new_tokens=80)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer