class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Intialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to command."""
        print(f"{self.name} is now sitting!")

    def roll_back(self):
        """Simulates a dog rolling over in response to command."""
        print(f"{self.name} rolled over!")
