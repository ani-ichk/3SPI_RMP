from abc import ABC, abstractmethod


class AbstractUsersHelper(ABC):
    @abstractmethod
    def get_user_password(self, username) -> str:
        """
        :param:
        :return:
        """

    def validate_username(self, username: str) -> str:
        pass

    def check_passwords_match(
            cls,
            password1: str,
            password2: str,
    ):
        return password1 == password2

    def validate_user_password(self, username: str, password: str) -> bool:
        db_password = self.get_user_password(username)
        if db_password is None:
            return False
        return self.check_passwords_match(
            password1 = db_password,
            password2 = password,
        )