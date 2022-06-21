import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import index, test

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(index.router)
app.include_router(test.router)

# if __name__ == '__main__':
#     # コンソールで [$ uvicorn run:app --reload]でも可
#     uvicorn.run(app=app)