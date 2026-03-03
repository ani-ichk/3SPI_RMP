import secrets

# генерация трёх случайных токенов
API_TOKENS = frozenset(
    secrets.token_hex(16) for _ in range(3)
)
# print(API_TOKENS)