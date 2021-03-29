# Simple RBAC
This is a simple implementation of Basic RBAC

It provides basic functions such as:
 `create_user`,`login_user`, `logout`, `update_role`,
`access_resource`, `get_all_users`

Admin user by default doesn't have any role, but
it can give roles, and access to other users &
itself

you can run the interface by:
`python interface.py`

You can also create a object of RBAC class
and perform basic operation, check sample_usage.py
for examples.



### High Level Diagram

![High Level Diagram](/docs/Archi.PNG?raw=true)
