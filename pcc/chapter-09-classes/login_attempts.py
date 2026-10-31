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


new_user = User("Li Hong", "Wang", "45", "M", "chinese")
new_user.describe_user()

new_user.show_login_attempts()

new_user.increment_login_attempts()
new_user.show_login_attempts()

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.show_login_attempts()

new_user.reset_login_attempts()
new_user.show_login_attempts()
