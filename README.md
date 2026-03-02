# AI Document Analyzer
#Day 1
- FastAPI app that summarizes text, extracts keywords, and analyzes sentiment  
- Uses HuggingFace `google/flan-t5-small` (CPU friendly)  
- Endpoints:
  - POST /analyze/summarize
  - POST /analyze/keywords
  - POST /analyze/sentiment
- Fully local, no cloud needed
