# AI Document Analyzer

A full-stack AI-powered document analysis application built with FastAPI and open-source transformer models. Upload documents or paste text to get instant summaries, keyword extraction, sentiment analysis, and an interactive chat interface powered by retrieval-augmented generation (RAG).
Live demo: https://ai-doc-analyzer-frontend.s3.us-east-2.amazonaws.com/index.html

![DocMind AI Document Analyzer] (Analyze_File.png)
![DocMind AI Document Analyzer] (Summarize_text.png)


## Features

Document upload — supports PDF, DOCX, and TXT files
Text summarization — generates concise summaries using Google flan-t5-small
Keyword extraction — identifies the most significant terms from any document
Sentiment analysis — detects positive, negative, or neutral tone
Document chat (RAG) — ask questions about uploaded documents using FAISS vector search and semantic embeddings

## Technology Stack

Tech stack
Layer                                    Technology
Backend                                 FastAPI, Python 3.11, Uvicorn
AI models                               google/flan-t5-small, sentence-transformers/all-MiniLM-L6-v2
Vector search                           FAISS (Facebook AI Similarity Search)
File parsing                            pypdf, python-docx
Frontend                                Vanilla HTML/CSS/JS, hosted on AWS S3
Infrastructure                          AWS EC2 (t3.small), CloudFront CDN
CI/CD                                   GitHub Actions
Process management                      systemd

## Project Structure

User Browser
     │
     ▼
AWS S3 (static frontend)
     │  HTTPS API calls
     ▼
AWS CloudFront (HTTPS termination)
     │
     ▼
EC2 t3.small (FastAPI + Uvicorn)
     │
     ├── flan-t5-small (summarization + sentiment)
     ├── all-MiniLM-L6-v2 (document embeddings)
     └── FAISS index (vector similarity search)
## API endpoints
Method             Endpoint                 Description
POST             /analyze/file          Upload and analyze a document
POST             /analyze/summarize     Summarize text input
POST             /analyze/keywords      Extract keywords from text
POST             /analyze/sentiment     Analyze sentiment of text
POST             /ai/chat               Chat with an uploaded document
GET              /health                 Health check

## Project Structure

ai-document-analyzer/
├── app/
│   ├── main.py                  # FastAPI app entry point
│   ├── core/
│   │   ├── config.py            # Settings via pydantic-settings
│   │   └── logger.py            # Logging configuration
│   ├── routes/
│   │   ├── analyze.py           # File upload and text analysis routes
│   │   └── chat.py              # Document chat route
│   ├── services/
│   │   ├── ai_service.py        # flan-t5 model — summarize, sentiment, keywords
│   │   ├── vector_store.py      # FAISS index and document store
│   │   └── document_chat_service.py  # RAG pipeline
│   ├── utils/
│   │   ├── file_parser.py       # PDF, DOCX, TXT extraction
│   │   └── text_chunker.py      # Split documents into chunks
│   └── templates/
│       └── index.html
├── tests/
│   └── test_health.py
├── .github/
│   └── workflows/
│       └── deploy.yml           # CI/CD pipeline
├── requirements.txt
└── README.md

## Local development

1. Clone the repository
   
   git clone https://github.com/<your-username>/ai-document-analyzer.git
   cd ai-document-analyzer
   
2. Create and activate a virtual environment

   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   
3. Install dependencies

   pip install -r requirements.txt

4. Create .env file

   echo "APP_NAME=AI Document Analyzer
   MODEL_NAME=google/flan-t5-small
   MAX_NEW_TOKENS=150" > .env
   
5. Run the application
   
   uvicorn app.main:app --reload
   
6. Open the app in your browser
   
   http://localhost:8000/docs to explore the API
   

## Deployment

The application is deployed on AWS using the following setup:
Server setup (EC2 t3.small, Ubuntu 22.04):

Add swap for model loading on low-memory instance
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Install dependencies
python3 -m venv ~/venv
source ~/venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt

Process management: systemd service keeps the app running and restarts it automatically on failure.
CI/CD: GitHub Actions runs tests on every push to main and deploys to EC2 via SSH.


## Notes

- The application is designed as a backend-first document intelligence service.
- Document chat is built on a simple retrieval workflow using text chunking.
- Current file upload support includes PDF, DOCX, and TXT.

## Key design decisions

Single model for multiple tasks — flan-t5-small handles both summarization and sentiment analysis via prompt engineering, avoiding the memory cost of loading a separate sentiment model on a 2GB RAM instance.

CPU-only PyTorch — the EC2 t3.small has no GPU. Installing the CPU-only torch build saves ~1.5GB of disk space and works within the instance's memory constraints.

In-memory FAISS index — document vectors are stored in memory for fast retrieval. The index resets on server restart, which is acceptable for a personal project. For persistence, faiss.write_index() could be used to save the index to disk.

One uvicorn worker — running multiple workers would load the AI models multiple times, exhausting the 2GB RAM. A single worker with async routing handles concurrent requests efficiently for low traffic.

## Environment variables
Variable            Default              Description
APP_NAME        AI Document Analyzer    Application name
MODEL_NAME      google/flan-t5-small    HuggingFace model to use
MAX_NEW_TOKENS   150                    Maximum tokens for generation