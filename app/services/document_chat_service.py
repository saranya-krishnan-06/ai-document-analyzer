# services/document_chat_service.py
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import faiss
import numpy as np

# Load embedding model
#embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

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

    if not chunks:
        return
    
    vectors = embedding_model.encode(chunks)
    vectors = np.array(vectors, dtype="float32")
    index.add(vectors)

    for chunk in chunks:
        documents.append(chunk)


def search_similar_chunks(query, k=3):
    embedding_model, _, _ = load_models() 

    if not documents:
        return[]
    
    query_vector = embedding_model.encode([query])
    query_vector = np.array(query_vector, dtype="float32")


    distances, indices = index.search(query_vector, k)

    results = []
    for idx in indices[0]:
        if 0 <= idx < len(documents):
            results.append(documents[idx])

    return results

def answer_question(question: str):
    _, tokenizer, model = load_models() 
    chunks = search_similar_chunks(question)

    if not chunks:
        return "I couldn't find relevant information in the uploaded document."

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

    outputs = model.generate(**inputs, max_new_tokens=80)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    return answer