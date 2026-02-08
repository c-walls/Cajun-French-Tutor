import os
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path

app = FastAPI(title="Cajun French Tutor")
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Locate static directory: ../frontend/static
STATIC_DIR = Path(__file__).resolve().parents[1] / "frontend" / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

chat_history = []
print(f"DEBUG: Gemini Key is: {api_key}")

@app.get("/")
async def root():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/chat", response_class=HTMLResponse)
async def chat(message: str = Form(...)):
    chat_history.append({"role": "user", "content": message})

    # Gemini used as a standin for testing
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=chat_history,
        config={'system_instruction': "You are a helpful Cajun French tutor."}
    )
    
    bot_response = response.text
    chat_history.append({"role": "bot", "content": bot_response})
    
    # 4. Return pre-rendered HTML fragments
    return f"""
        <article class="bubble user">{message}</article>
        <article class="bubble bot">{bot_response}</article>
        """

