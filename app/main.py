import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
ROOT_PROJECT_DIR = BASE_DIR.parent
TEMPLATE_DIR = ROOT_PROJECT_DIR / "html"

app = FastAPI()
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@app.get('/')
def read_index(request: Request):
    context = {
        "request":request,
        "title":"Fast API",
    }
    return templates.TemplateResponse("index.nginx-debian.html", context)

@app.get("/abc")
def abc():
    return {"abc":"world"}