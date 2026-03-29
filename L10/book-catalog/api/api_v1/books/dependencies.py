from typing import Annotated

from fastapi import (
    HTTPException,
    status,
    Request,
)
from fastapi.params import Depends

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
)


from .crud import storage
from api.api_v1.auth.services.redis_tokens_halper import redis_tokens
from api.api_v1.auth.services.redis_users_helper import RedisUsersHelper
from schemas.book import Book
from core import config



UNSAFE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)

api_token_auth = HTTPBearer(
    scheme_name="Api token",
    description="Enter your **API token**",
    auto_error=False,
)

basic_user_auth = HTTPBasic(
    scheme_name="User auth",
    description="Enter your **username + password**",
    auto_error=False,
)

redis_users = RedisUsersHelper(
    port=config.REDIS_PORT,
    host=config.REDIS_HOST,
    db=config.REDIS_DB_USERS,
)


def prefetch_book(slug: str) -> Book:
    book = storage.get_by_slug(slug=slug)
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Slug {slug!r} not found",
    )


def validate_api_token(
    api_token: HTTPAuthorizationCredentials,
):
    if not redis_tokens.token_exists(api_token.credentials):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API token",
        )


def api_token_required(
    request: Request,
    api_token: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(api_token_auth),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    if not api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API token is required",
        )

    validate_api_token(api_token=api_token)


def validate_basic_auth(
    credentials: HTTPBasicCredentials | None,
):
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    if not redis_users.validate_user_password(
        username=credentials.username,
        password=credentials.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )


def user_auth_required(
    request: Request,
    credentials: Annotated[
        HTTPBasicCredentials | None,
        Depends(basic_user_auth),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    validate_basic_auth(credentials=credentials)


def user_auth_or_api_token_required(
    request: Request,
    api_token: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(api_token_auth),
    ] = None,
    credentials: Annotated[
        HTTPBasicCredentials | None,
        Depends(basic_user_auth),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    if credentials:
        return validate_basic_auth(credentials=credentials)
    if api_token:
        return validate_api_token(api_token=api_token)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="API token or basic auth required",
    )
