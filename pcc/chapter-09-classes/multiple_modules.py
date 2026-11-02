import regular_user_module as users_module  # noqa: F401, I001
import admin_module


new_admin = admin_module.Admin("Robert", "Mason", 42, "Trans-F", "Greek")
new_admin.greet_user()
new_admin.admin_privileges.show_priveleges()
