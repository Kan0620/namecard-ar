from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='static')

@router.get("/test_ar", response_class=HTMLResponse)
async def test_ar(request: Request):
    return templates.TemplateResponse(
        "embed_index.html",
        {
            "request": request,
            "obj_file_path": "data/first_test.glb",
            "marker_img_path": "data/pattern-marker.patt"
            }
    )
