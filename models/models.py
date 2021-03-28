from enum import IntEnum
from helper.utils import auto_str


class UserType(IntEnum):
    NORMAL_USER = 1
    ADMIN_USER = 2


class ActionType(IntEnum):
    READ = 1
    WRITE = 2
    DELETE = 3


class ResourcesType(IntEnum):
    """
    Static list of Resources like disks, VM, web server, SQL
    """
    RESOURCE_1 = 1
    RESOURCE_2 = 2
    RESOURCE_3 = 3


@auto_str
class User:
    def __init__(self, user_id, user_type, details):
        self._userType = user_type
        self._userId = user_id
        self.details = details

    def get_id(self):
        return self._userId

    def get_type(self):
        return self._userType


@auto_str
class Role:
    """
    Action on a resource is resource
    """

    def __init__(self, resource_actions):
        self._permissions = resource_actions

    def update_role(self, permissions):
        self._permissions = permissions

    def update_access_for_resources(self, permission):
        for k, v in permission:
            self._permissions[k] = v

    def get_access_level_for_resource(self, resource):
        if resource in self._permissions:
            return self._permissions[resource]
        else:
            return -1

    ## Some predefined Roles for ease
    @classmethod
    def developer_role(cls):
        permissions = {
            ResourcesType.RESOURCE_1: ActionType.DELETE,
            ResourcesType.RESOURCE_2: ActionType.READ
        }
        return cls(permissions)

    @classmethod
    def sql_developer_role(cls):
        permissions = {
            ResourcesType.RESOURCE_2: ActionType.DELETE,
            ResourcesType.RESOURCE_3: ActionType.READ
        }
        return cls(permissions)

    @classmethod
    def app_developer_role(cls):
        permissions = {
            ResourcesType.RESOURCE_1: ActionType.READ,
            ResourcesType.RESOURCE_3: ActionType.READ,
            ResourcesType.RESOURCE_2: ActionType.DELETE
        }
        return cls(permissions)
