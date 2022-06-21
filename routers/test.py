from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="static")

@router.get("/test", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse(
        "template_ar.html",
        {
            "request": request,
            "obj_file_path": "/ar_data/test/test.glb",
            "marker_img_path": "/ar_data/test/test.patt"
            }
    )

