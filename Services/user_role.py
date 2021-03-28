from models.models import UserType, Role, ResourcesType
from helper.utils import auto_str


@auto_str
class UserRole:
    """
    This service manges all user_id & role related interactions
    """

    def __init__(self):
        self._user_role = {}

    def _add_user(self, user_id):
        """
        Adds a new user_id if not already present
        """
        if user_id not in self._user_role:
            self._user_role[user_id] = []

    @staticmethod
    def can_user_update_roles(current_user):
        return current_user.get_type() == UserType.ADMIN_USER

    def _update_user_roles(self, current_user, user_id, permission):
        """
        Gives roles to the user_id
        """
        assert type(permission) == Role
        if not self.can_user_update_roles(current_user):
            raise Exception("User Doesn't have permission to update roles")

        self._add_user(user_id)
        if permission not in self._user_role[user_id]:
            self._user_role[user_id].append(permission)
        else:
            self._user_role[user_id] = permission

    def _get_roles_for_user(self, user_id):
        return self._user_role[user_id]

    def _access_resource_for_user(self, curr_user_id, resource):
        """
        :param curr_user_id:
        :param resource:
        :return: max level of access for a resource, returns -1 in case of no access
        """
        assert type(resource) == ResourcesType
        roles = self._get_roles_for_user(curr_user_id)
        # find all roles user_id has access to and return max access available
        max_access = -1
        for role in roles:
            access = role.get_access_level_for_resource(resource)
            if access != -1:
                if max_access == -1:
                    max_access = access
                else:
                    max_access = max(max_access, access)
        return max_access
