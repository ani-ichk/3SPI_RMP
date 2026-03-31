from redis import Redis
from book_catalog.api.api_v1.auth.services.tokens_helper import AbstractTokensHelper
from book_catalog.core import config


class RedisTokensHelper(AbstractTokensHelper):
    def __init__(self):
        self.redis = Redis(
            port=config.REDIS_PORT,
            host=config.REDIS_HOST,
            db=config.REDIS_DB_TOKENS,
            decode_responses=True
        )
        self.token_name = config.REDIS_TOKENS_SET_NAME

    def token_exists(self, token: str) -> bool:
        return self.redis.exists(self.token_name)

    def add_token(self, token: str):
        self.redis.sadd(self.token_name, token)

    def get_tokens(self) -> list[str]:
        return list(self.redis.smembers(self.token_name))

    def delete_token(self, token: str):
        self.redis.srem(self.token_name, token)


redis_tokens = RedisTokensHelper()