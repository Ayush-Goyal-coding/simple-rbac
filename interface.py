from rbac import RBAC
from models.models import Role, ResourcesType
rbac = RBAC()
#print(str(rbac._get_current_user()))
# rbac.logout()
while(True):

    print("Hi You are logged in as ",rbac._get_current_user().get_id())
    print("Press 1 to Create a new User. Only Admins can create a new User")
    print("Press 2 to view roles of current user")
    print("Press 3 to update role of a user")
    print("Press 4 to login as different User")
    print("Press 5 to View all users")
    print("Press 6 to access a Resource")

    option = int(input())
    try:
        if option == 1:
            print("Enter UserID")
            userID = input()
            print("Enter password")
            password = input()
            print("Enter Type of you want to create: A - Admin/N- Normal")
            userType = input()
            assert (userType in ['A','N'])
            rbac.create_user(user_id=userID,password=password,user_type=userType)

        elif option==2:
            roles = rbac.view_role()
            for role in roles:
                print(str(role))
        elif option==3:
            print("Enter UserID:")
            userID = input()
            print("choose Role you want to enter: ")
            print("Press 1 for APP developer")
            print("Press 2 for SQL developer")
            print("Press 3 for general developer role")
            print("You can also create custom role, checks docs for the same")
            option_3_sub = int(input())
            assert option_3_sub in [1,2,3]
            if option_3_sub == 1:
                role = Role.app_developer_role()
            elif option_3_sub ==2:
                role =  Role.sql_developer_role()
            elif option_3_sub==3:
                role = Role.developer_role()
            else:
                print("invalid")
            rbac.update_role("ayush", role)
        elif option==4:
            print("Enter UserID")
            userID = input()
            print("Enter password")
            password = input()
            rbac.login_user(user_id=userID,password=password)
        elif option==5:
            print(rbac.get_all_users())
        elif option==6:
            cnt = 1
            dct = {}
            for i in ResourcesType:
                print("Press "+str(cnt)+" for "+i.name)
                dct[cnt] = i

                cnt += 1
            option_6_sub = int(input())
            rbac.access_resource(dct[option_6_sub])
        else:
            print("invalid option selected")
    except Exception as e:
        print(e)