from es_9_11 import *

user: User = User("Marcel", "Movileanu", "mobsung", "blabla@gmail.com")
privileges: Privileges = Privileges()
privileges.set_privileges()

admin: Admin = Admin(user, privileges)

admin.show_info()