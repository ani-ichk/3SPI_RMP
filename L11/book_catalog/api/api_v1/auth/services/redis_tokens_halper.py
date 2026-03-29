from redis import Redis
from book_catalog.api.api_v1.auth.services.tokens_helper import AbstractTokensHelper
from book_catalog.core import config


class RedisTokensHelper(AbstractTokensHelper):
    def __init__(self, port: int, host: str, db: int, set_name_tokens: str):
        self.redis = Redis(
            port=port,
            host=host,
            db=db,
            decode_responses=True
        )
        self.token_name = set_name_tokens

    def token_exists(self, token: str) -> bool:
        return self.redis.exists(self.token_name)

    def add_token(self, token: str):
        self.redis.sadd(self.token_name, token)


redis_tokens = RedisTokensHelper(
    port=config.REDIS_PORT,
    host=config.REDIS_HOST,
    db=config.REDIS_DB,
    set_name_tokens=config.REDIS_TOKENS_SET_NAME,
)