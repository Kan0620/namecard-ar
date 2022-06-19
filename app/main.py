from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.mount("/", StaticFiles(directory="/app/pages", html=True), name="static")
