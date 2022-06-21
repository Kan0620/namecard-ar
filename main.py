# from typing import List

# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()


# app.mount("/", StaticFiles(directory="/app/pages", html=True), name="static")
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='pages')


@app.get("/", response_class=HTMLResponse)
#@router.get("/", response_class=HTMLResponse)
def get_product(request: Request):
    return templates.TemplateResponse(
        "index.html",
    )

# if __name__ == '__main__':
#     # コンソールで [$ uvicorn run:app --reload]でも可
#     uvicorn.run(app=app)