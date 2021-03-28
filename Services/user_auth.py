from models.models import UserType, User
from helper.utils import auto_str


@auto_str
class UserAuth:
    def __init__(self):
        self._userPasswords = {}
        self._userId_user = {}

    def _create_user(self, user_id, password, user_type=UserType.NORMAL_USER, details=None):
        if details is None:
            details = {}
        if user_id in self._userPasswords:
            raise Exception("User is already Present")
        user = User(user_id=user_id, user_type=user_type, details=details)
        self._userPasswords[user_id] = password
        self._userId_user[user_id] = user
        return user

    def _verify_user(self, user_id, password):
        return self._userPasswords[user_id] == password

    def _get_all_users(self):
        return self._userPasswords.keys()

    def _get_user_by_id(self, user_id):
        return self._userId_user[user_id]