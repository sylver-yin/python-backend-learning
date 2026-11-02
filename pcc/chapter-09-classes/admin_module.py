from regular_user_module import User


class AdminPriveleges:
    """Describes an admin's privileges on a site."""

    def __init__(self):
        """Initialise admin's privileges."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can unban user",
            "cannot be banned",
        ]

    def show_priveleges(self):
        """Print a statement about administrator privileges and loop through a list of them."""
        print("Administrator has these priveleges:")
        for privilege in self.privileges:
            print(f"x {privilege}")


class Admin(User):
    """A simple simulation of an admin profile."""

    def __init__(self, first_name, last_name, age, gender, nationality):
        """Initialise the admin profile user info."""
        super().__init__(first_name, last_name, age, gender, nationality)
        self.admin_privileges = AdminPriveleges()
