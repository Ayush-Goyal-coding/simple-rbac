from Services.user_auth import UserAuth
from Services.user_role import UserRole, UserType
from helper.utils import auto_str


@auto_str
class RBAC:
    def __init__(self):
        self._userRole = UserRole()
        self._userAuth = UserAuth()
        admin_user = self._userAuth._create_user(user_id='admin', password="admin",
                                                 user_type=UserType.ADMIN_USER)
        self._currentUser = admin_user

    def get_current_user(self):
        return self._currentUser

    def is_admin(self):
        self._validate()
        return self._currentUser.get_type() == UserType.ADMIN_USER

    def create_user(self, user_id, password, user_type=UserType.NORMAL_USER, details=None):
        self._validate()
        if self.is_admin():
            return self._userAuth._create_user(user_id, password, user_type, details)
        else:
            raise Exception("Only Admins are allowed to create users")

    def login_user(self, user_id, password):
        self._validate()
        if self._userAuth._verify_user(user_id, password):
            self._currentUser = self._userAuth._get_user_by_id(user_id)

    def logout(self):
        self._currentUser = None

    def update_role(self, user_id, permissions):
        return self._userRole._update_user_roles(self._currentUser, user_id, permissions)

    def view_role(self):
        return self._userRole._get_roles_for_user(self._currentUser.get_id())

    def access_resource(self, resource):
        return self._userRole._access_resource_for_user(self._currentUser.get_id(), resource)

    def get_all_users(self):
        return self._userAuth._get_all_users()

    def _validate(self):
        if self._currentUser is None:
            raise Exception("Please Login as a User and Try")
