from .users_helper import AbstractUsersHelper

from redis import Redis


class RedisUsersHelper(AbstractUsersHelper):
    def __init__(self, port: int, host: str, db: int):
        self.redis = Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )

    def get_user_password(self, username) -> str | None:
        return self.redis.get(username)
