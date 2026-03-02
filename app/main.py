from fastapi import FastAPI
from app.routes.analyze import router as analyze_router

app = FastAPI(title="AI Document Analyzer API")
app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])

@app.get("/")
def read_root():
    return {"message": "AI Document Analyzer is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}