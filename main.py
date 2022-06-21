# from typing import List

# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()


# app.mount("/", StaticFiles(directory="/app/pages", html=True), name="static")
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='static')


@app.get("/", response_class=HTMLResponse)

def get_product(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# if __name__ == '__main__':
#     # コンソールで [$ uvicorn run:app --reload]でも可
#     uvicorn.run(app=app)