from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path

app = FastAPI(title="Cajun French Tutor")

# static directory: ../frontend/static
STATIC_DIR = Path(__file__).resolve().parents[1] / "frontend" / "static"
if not STATIC_DIR.exists():
    raise SystemExit(f"Static directory not found: {STATIC_DIR}")

# Serve the static files at /static
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
