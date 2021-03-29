from rbac import RBAC
from models.models import Role, ResourcesType, ActionType
rbac = RBAC()
rbac.create_user('ayush', password='password')
rbac.update_role('ayush', Role.developer_role())
custom_permissions  = {
    ResourcesType.RESOURCE_2: ActionType.DELETE,
    ResourcesType.RESOURCE_3: ActionType.DELETE
}
custom_role = Role(custom_permissions)
rbac.update_role('ayush', custom_role)

rbac.login_user('ayush', 'password')
roles = rbac.view_role()
for role in roles:
    print(role)

# This gives Highest allowed permission for this resource for the current user
print(rbac.access_resource(ResourcesType.RESOURCE_2))