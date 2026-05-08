from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import date, datetime
from fastapi import Request

BASE_DIR = Path(__file__).resolve().parent.parent

def inject_current_date_and_dt(
        request: Request,
) -> dict[str, date]:
    return {
        "today": date.today(),
        "now": datetime.now(),
    }

templates = Jinja2Templates(
    directory=BASE_DIR / "templates",
    context_processors=[
        inject_current_date_and_dt,
    ],
)