from rbac import RBAC
from models.models import Role,ResourcesType
rbac = RBAC()
print(str(rbac._get_current_user()))
# rbac.logout()

user1 = rbac.create_user("ayush", "password")
roleForUser1 = Role.developer_role()
role2 = Role.app_developer_role()
role3 = Role.sql_developer_role()
rbac.update_role("ayush", roleForUser1)

# print(rbac.)
# print(str(rbac._get_all_users()))
rbac.login_user("ayush", "password")
print(str(rbac.view_role()[0]))
try:
    rbac.update_role('ayush', role2)  #will
except:
    print("Not Allowed")

print(rbac.access_resource(ResourcesType.RESOURCE_2))
print(rbac.access_resource(ResourcesType.RESOURCE_1))
