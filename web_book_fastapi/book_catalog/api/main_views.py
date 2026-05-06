from fastapi import APIRouter, Request
from datetime import date

from pyexpat import features
from starlette.responses import HTMLResponse
from templating.jinja_templates import templates


router = APIRouter()

@router.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema = False,
)
def read_root(request: Request) -> HTMLResponse:
    context = {}
    year = date.today().year
    features = [
        "Create books",
        "Real time statistics",
        "Management",
    ]
    context.update(
        request=request,
        year=year,
        features=features,
    )
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=context,
    )