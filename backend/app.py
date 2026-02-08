import os
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path
from google import genai

app = FastAPI(title="Cajun French Tutor")

# Locate static directory: ../frontend/static
STATIC_DIR = Path(__file__).resolve().parents[1] / "frontend" / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Setup gemini chat session for testing
chat_history = []
client = genai.Client()
chat = client.chats.create(
    model="gemini-2.5-flash",
    config={'system_instruction': "You are a helpful Cajun French tutor."}
)


@app.get("/")
async def root():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):
    chat_history.append({"role": "user", "content": message})

    # Gemini used as a standin for testing
    response = chat.send_message(message)
    bot_response = response.text
    chat_history.append({"role": "bot", "content": bot_response})
    
    # Return pre-rendered HTML fragments
    return f"""
        <article class="bubble user">{message}</article>
        <article class="bubble bot">{bot_response}</article>
        """

