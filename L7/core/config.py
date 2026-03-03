import secrets

# генерация трёх случайных токенов
API_TOKENS = frozenset(
    secrets.token_hex(16) for _ in range(3)
)

USER_DB = {
    "admin": "1234",
    "user": "qwerty",
}