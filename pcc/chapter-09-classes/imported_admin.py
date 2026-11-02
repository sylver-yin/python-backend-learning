from users_module import User, AdminPriveleges, Admin  # noqa: F401, I001

admin_user = Admin("James", "Valstrax", "35", "M", "Japanese")
admin_user.greet_user()
admin_user.admin_privileges.show_priveleges()
