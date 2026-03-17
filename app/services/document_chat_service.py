# services/document_chat_service.py
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

# LLM
embedding_model = None
tokenizer = None
model = None

def load_models():
    global embedding_model, tokenizer, model

    if embedding_model is None:
        embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    if tokenizer is None or model is None:
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    return embedding_model, tokenizer, model

def add_document_chunks(chunks):
    embedding_model, _, _ = load_models()
    vectors = embedding_model.encode(chunks)
    index.add(np.array(vectors))

    for chunk in chunks:
        documents.append(chunk)


def search_similar_chunks(query, k=5):
    embedding_model, _, _ = load_models() 
    query_vector = embedding_model.encode([query])

    distances, indices = index.search(np.array(query_vector), k)

    results = []
    for i, idx in enumerate(indices[0]):
        if idx < len(documents) and distances[0][i] < 1.5:
            results.append(documents[idx])

    return results

def answer_question(question):
    embedding_model, _, _ = load_models() 
    chunks = search_similar_chunks(question)

    context = " ".join(chunks)

    prompt = f"""
You are an AI assistant.

Use ONLY the provided context to answer the question.
If the answer is not in the context, say:
"I don't know based on the document."

Give a clear and complete answer.

Context:
{context}

Question:
{question}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(**inputs, max_new_tokens=120)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Clean unwanted text
    answer = answer.replace(prompt, "").strip()
    return answer