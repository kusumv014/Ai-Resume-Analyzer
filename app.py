from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from llm_engine import analyze_resume

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html") as f:
        return f.read()

@app.post("/analyze", response_class=HTMLResponse)
def analyze(resume: str = Form(...)):
    result = analyze_resume(resume)

    return f"""
    <html>
    <head>
    <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
    <div class="container">
    <h2>Result</h2>
    <pre>{result}</pre>
    <a href="/">Back</a>
    </div>
    </body>
    </html>
    """
    