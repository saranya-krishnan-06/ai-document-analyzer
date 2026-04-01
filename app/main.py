# app/main.py
import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from app.routes.analyze import router as analyze_router
from app.routes.chat import router as chat_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="app/templates")

app = FastAPI(title="AI Document Analyzer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dwlf85sg0bufi.cloudfront.net",
        "https://ai-doc-analyzer-frontend.s3.us-east-2.amazonaws.com",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])
app.include_router(chat_router, prefix="/ai", tags=["Chat"])


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health_check():
    return {"status": "healthy"}
