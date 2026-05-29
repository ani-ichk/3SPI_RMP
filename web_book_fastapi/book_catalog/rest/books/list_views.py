from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from storage.books.crud import storage
from templating.jinja_templates import templates
from dependencies.books import GetBooksStorage


router = APIRouter()

@router.get(
    "/",
    name="books:list",
    response_class=HTMLResponse,
)
def list_view(
        request: Request,
) -> HTMLResponse:
    context = {
        "books": storage.get_all(),
    }

    return templates.TemplateResponse(
        request=request,
        name="books/list.html",
        context=context,
    )