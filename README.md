# AI Document Analyzer
A production-ready FastAPI-based AI microservice that performs:

 1.Text Summarization

 2.Keyword Extraction

 3.Sentiment Analysis

Built with clean architecture principles, configuration management, logging, and testing — designed to reflect real-world backend + DevOps practices.

Goals:
1.AI model integration (local, no external APIs)
2.Backend API development with FastAPI
3.Clean architecture & config management
4.Testing with pytest
5.Git & version control best practices
6.Docker & CI/CD (coming next)

Architecture Overview
ai-document-analyzer/
│
├── app/
│   ├── core/          # Config & logging
│   ├── routes/        # API endpoints
│   ├── services/      # AI logic
│   └── main.py        # FastAPI app entrypoint
│
├── tests/             # Unit tests
├── pytest.ini         # Test config
└── README.md

AI Model

1.Model: google/flan-t5-small
2.Runs locally (CPU-friendly)
3.No OpenAI or paid APIs required
4.Uses HuggingFace Transformers

Tech Stack

1.Python 3.12
2.FastAPI
3.HuggingFace Transformers
4.Pydantic v2
5.pytest
6.Git

Running Locally
Step 1️: Clone Repository
  git clone https://github.com/<your-username>/ai-document-analyzer.git
  cd ai-document-analyzer

Step 2: Create Virtual Environment
  python -m venv venv
  source venv/Scripts/activate   # Windows Git Bash

Step 3: Install Dependencies 
  pip install -r requirements.txt

Step 4: Start Server
  uvicorn app.main:app --reload

Step 5: Open browser:http://127.0.0.1:8000/docs 

API Endpoints

Summarize Text : POST /analyze/summarize
Extract Keywords : POST /analyze/keywords
Analyze Sentiment : POST /analyze/sentiment 

Configuration Management
Uses Pydantic v2 settings:
    MODEL_NAME = "google/flan-t5-small"
    MAX_NEW_TOKENS = 150

Production-Ready Features

    Structured logging
    Error handling
    Config abstraction
    Modular architecture
    Test coverage
    Git workflow management

Next Steps
    Dockerize application
    Add GitHub Actions CI pipeline
    Add health checks & metrics
    Deploy to container environment

Author

Saranya Krishnan
Cloud Engineer | AWS | Backend | DevOps Enthusiast

This Project demonstrates: 
    Backend engineering
    Clean architecture
    Dependency debugging
    Git conflict resolution
    Production mindset
    DevOps preparation

