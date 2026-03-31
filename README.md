# AI Document Analyzer

AI Document Analyzer is a FastAPI-based backend for extracting intelligence from PDF, DOCX, and TXT documents. It provides document summarization, keyword extraction, sentiment analysis, and document-based chat using a retrieval workflow.

## Features

- Upload and analyze documents
- Extract text from PDF, DOCX, and TXT files
- Generate summaries from document content
- Extract keywords automatically
- Analyze sentiment for document text
- Upload documents for question-answering via document chat
- Clean API design with separate analysis and document chat routes

## API Endpoints

- `GET /` - Home page
- `GET /health` - Health check
- `POST /analyze/file` - Upload a document and receive summary, sentiment, keywords
- `POST /analyze/summarize` - Summarize plain text
- `POST /analyze/keywords` - Extract keywords from plain text
- `POST /analyze/sentiment` - Analyze sentiment of plain text
- `POST /document/upload` - Upload a document for chat context
- `POST /document/chat` - Ask a question against uploaded document content

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- Jinja2
- Transformers
- PyTorch
- Sentence Transformers
- FAISS CPU
- PyPDF
- python-docx
- python-multipart

## Project Structure

- `app/main.py` - FastAPI application setup
- `app/routes/analyze.py` - Document analysis endpoints
- `app/routes/document_chat.py` - Document upload and chat endpoints
- `app/services/ai_service.py` - Text summarization, keyword extraction, sentiment analysis
- `app/services/document_chat_service.py` - Document chunk handling and question answering
- `app/services/file_service.py` - File text extraction service
- `app/services/vector_store.py` - Vector search utilities
- `app/utils/file_parser.py` - PDF, DOCX, and TXT parsing
- `app/utils/text_chunker.py` - Text chunking for retrieval
- `app/core/config.py` - Application configuration
- `app/core/logger.py` - Logging setup
- `app/templates/index.html` - Frontend template
- `tests/` - Unit tests

## Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/ai-document-analyzer.git
   cd ai-document-analyzer
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application
   ```bash
   uvicorn app.main:app --reload
   ```
5. Open the app in your browser
   ```
   http://127.0.0.1:8000
   ```

## Testing

Run tests with:

```bash
pytest
```

## Notes

- The application is designed as a backend-first document intelligence service.
- Document chat is built on a simple retrieval workflow using text chunking.
- Current file upload support includes PDF, DOCX, and TXT.

## Future Improvements

- Add Docker and deployment automation
- Improve document chat with better retrieval and memory
- Add support for external vector databases
- Add more robust UI and frontend integration
- Add production-ready configuration and logging

