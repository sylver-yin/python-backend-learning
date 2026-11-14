from creating_and_using_a_class import (
    Dog,
)  # NOTE: Could've done it without imports by doing it in previous file, just trying if I remember import syntax

my_dog = Dog("Lana", 9)
your_dog = Dog("Dina", 6)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")
your_dog.roll_back()
