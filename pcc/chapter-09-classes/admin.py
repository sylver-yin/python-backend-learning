class User:
    """Simple simulation of a user profile."""

    def __init__(self, first_name, last_name, age, gender, nationality):
        """Initialise the user's info."""
        self.first = first_name
        self.last = last_name
        self.full_name = f"{self.first.title()} {self.last.title()}"
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.login_attempts = 0

    def greet_user(self):
        print(f"\nHello, {self.full_name}!")

    def describe_user(self):
        print(
            f"User's fullname: {self.full_name}, age: {self.age}, sex: {self.gender}, nationality: {self.nationality}"
        )

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")


class Admin(User):
    """A simple simulation of an admin profile."""

    def __init__(self, first_name, last_name, age, gender, nationality):
        """Initialise the admin profile user info."""
        super().__init__(first_name, last_name, age, gender, nationality)
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


rory_the_admin = Admin("Rory", "Snow", 27, "F", "british")
rory_the_admin.describe_user()
rory_the_admin.show_priveleges()
