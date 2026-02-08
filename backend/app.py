from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path

app = FastAPI(title="Cajun French Tutor")

# Locate static directory: ../frontend/static
STATIC_DIR = Path(__file__).resolve().parents[1] / "frontend" / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

chat_history = []

@app.get("/")
async def root():
    return FileResponse(STATIC_DIR / "index.html")

@app.post("/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):
    chat_history.append({"role": "user", "content": message})

    # TODO: Pass history to the model to prompt for response
    bot_response = f"C'est bon! Context length is now {len(chat_history)}. You said: {message}"
    chat_history.append({"role": "bot", "content": bot_response})
    
    # 4. Return pre-rendered HTML fragments
    return f"""
        <article class="bubble user">{message}</article>
        <article class="bubble bot">{bot_response}</article>
        """

