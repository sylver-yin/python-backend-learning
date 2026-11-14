class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolled over.")


my_dog = Dog("Lana", 9)

print(f"My dog's name is {my_dog.name.title()}")
print(f"My dog's age is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()
