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

from routers import index, test_ar

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='static')


@app.get("/test", response_class=HTMLResponse)

def get_product(request: Request):
    return templates.TemplateResponse(
        "embed_index.html",
        {
            "request": request,
            "obj_file_path": "data/first_test.glb",
            "marker_img_path": "data/pattern-marker.patt"
            }
    )

app.include_router(index.router)
app.include_router(test_ar.router)

# if __name__ == '__main__':
#     # コンソールで [$ uvicorn run:app --reload]でも可
#     uvicorn.run(app=app)