from fastapi import FastAPI
from app.routes.analyze import router as analyze_router
import logging
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
#from app.routes.document_chat import router as doc_chat_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="app/templates")
app = FastAPI(title="AI Document Analyzer API")
app.include_router(analyze_router, prefix="/analyze", tags=["Analyze"])
#app.include_router(doc_chat_router, prefix="/document")
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/")
def read_root():
    return {"message": "AI Document Analyzer is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)