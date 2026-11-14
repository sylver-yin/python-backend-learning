class User:
    """Simple simulation of a user profile."""

    def __init__(self, first_name, last_name, age, gender, nationality):
        """Initialise the first and last name of a user"""
        self.first = first_name
        self.last = last_name
        self.full_name = f"{self.first.title()} {self.last.title()}"
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def greet_user(self):
        print(f"\nHello, {self.full_name}!")

    def describe_user(self):
        print(
            f"User's fullname: {self.full_name}, age: {self.age}, sex: {self.gender}, nationality: {self.nationality}"
        )


user_male = User("Sherlock", "Moriarty", 29, "M", "british")
user_felame = User("Chen Yao", "Li", 34, "F", "chinese")

user_male.greet_user()
user_male.describe_user()

user_felame.greet_user()
user_felame.describe_user()
