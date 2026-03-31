import secrets
from abc import ABC, abstractmethod


class AbstractTokensHelper(ABC):
    @abstractmethod
    def token_exists(self, token: str) -> bool:
        pass

    @abstractmethod
    def add_token(self, token: str):
        pass

    @abstractmethod
    def get_tokens(self) -> list[str]:
        pass

    @abstractmethod
    def delete_token(self, token: str):
        pass

    def generate_token(self) -> str:
        return secrets.token_urlsafe(16)

    def generate_and_save_token(self):
        token = self.generate_token()
        self.add_token(token)
        return token