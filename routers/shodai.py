from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="static")

@router.get("/shodai", response_class=HTMLResponse)
async def shodai(request: Request):
    return templates.TemplateResponse(
        "template_ar.html",
        {
            "request": request,
            "obj_file_path": "/ar_data/shodai/shodai.glb",
            "marker_img_path": "/ar_data/shodai/shodai.patt"
            }
    )