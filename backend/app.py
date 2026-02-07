from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse 
from pathlib import Path

app = FastAPI(title="Cajun French Tutor")

# static directory: ../frontend/static
STATIC_DIR = Path(__file__).resolve().parents[1] / "frontend" / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def root():
    return FileResponse(STATIC_DIR / "index.html")
