from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from templating.jinja_templates import templates


router = APIRouter()

@router.get(
    "/",
    name="home",
    response_class=HTMLResponse,
    include_in_schema = False,
)
def home_page(request: Request) -> HTMLResponse:
    context = {}
    features = [
        "Create books",
        "Real time statistics",
        "Management",
    ]
    context.update(
        request=request,
        features=features,
    )
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=context,
    )

@router.get(
    "/about",
    name="about",
    include_in_schema = False,
)
def about_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={
            "request": request,
        },
    )