# AI Document Intelligence Platform
An AI-powered document analysis and question-answering platform built using FastAPI, HuggingFace Transformers, FAISS, and AWS.

This system allows users to upload documents and perform:

    AI-based document summarization
    Keyword extraction
    Sentiment analysis
    Context-aware document chat (RAG architecture)

Designed as a cloud-ready backend system with CI/CD automation and modular AI architecture.
Built with clean architecture principles, configuration management, logging, and testing — designed to reflect real-world backend + DevOps practices.

Goals:
1.AI model integration (local, no external APIs)
2.Backend API development with FastAPI
3.Clean architecture & config management
4.Testing with pytest
5.Git & version control best practices
6.Docker & CI/CD (coming next)

                ARCHITECTURE OVERVIEW


User → FastAPI → Text Processing → Embeddings → FAISS
→ Context Retrieval → LLM → Response

Key Architecture Concepts:

Retrieval Augmented Generation (RAG)
Vector similarity search
AI service abstraction layer
Cloud-ready backend design
Modular inference pipeline

                  TECH STACK

Backend

    FastAPI
    Python
    Uvicorn

AI / NLP

    HuggingFace Transformers
    FLAN-T5
    Sentence Transformers
    FAISS

Document Processing

    PyPDF
    python-docx

DevOps

    GitHub Actions (CI/CD)
    AWS EC2

Testing

    Pytest

                    FEATURES
Document Processing
    Supports PDF, DOCX, and TXT
    Automatic text extraction
    Intelligent text chunking
    Vector embedding generation

AI Capabilities

    Transformer-based summarization (FLAN-T5)
    Keyword extraction using NLP heuristics
    Sentiment analysis pipeline
    Contextual document Q&A using RAG

Vector Search

    Semantic search using Sentence Transformers
    FAISS vector indexing
    Relevant chunk retrieval for LLM prompts

Document Chat

    Ask questions about uploaded documents
    Context-aware responses
    Retrieval-Augmented Generation design

Web Interface

    Lightweight UI for:
    File upload
    Text analysis
    Document chat

DevOps

    CI pipeline using GitHub Actions
    Automated testing with Pytest
    AWS EC2 deployment
    Modular architecture for scaling AI services

         PROJECT STRUCTURE
 app/
 ├── routes/
 │     ├── analyze.py
 │     ├── document_chat.py
 │
 ├── services/
 │     ├── ai_service.py
 │     ├── document_chat_service.py
 │
 ├── utils/
 │     ├── file_parser.py
 │     ├── text_chunker.py
 │
 ├── core/
 │     ├── config.py
 │     ├── logger.py
 │
 ├── templates/
 │     ├── index.html
 │
 └── main.py

tests/
requirements.txt
Dockerfile (optional)
.github/workflows/

            Getting Started
Clone Repository
    git clone https://github.com/<your-username>/ai-document-analyzer.git
    cd ai-document-analyzer
Create Virtual Environment
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
Install Dependencies
    pip install -r requirements.txt
    Run Application
    uvicorn app.main:app --reload

Open:
    http://127.0.0.1:8000

Running Tests
    pytest

Deployment

The application can be deployed on:

    AWS EC2
    Docker containers
    Future support for:
      AWS ECS
      Kubernetes 

Future Improvements
    Streaming LLM responses
    Multi-document chat memory
    Vector database (Pinecone / Weaviate)
    Async embedding pipeline
    Production inference service
    CloudFormation / Terraform infra
    Model quantization for low-cost deployment

Future Improvements

    Streaming LLM responses
    Multi-document chat memory
    Vector database (Pinecone / Weaviate)
    Async embedding pipeline
    Production inference service
    CloudFormation / Terraform infra
    Model quantization for low-cost deployment


Author

Saranya Krishnan
Cloud Engineer | AWS | Backend | DevOps Enthusiast

