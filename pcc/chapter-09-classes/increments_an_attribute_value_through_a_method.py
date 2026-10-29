class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialise given information about a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Gives a descrptive name, neatly organised."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set odometer reading to the given value. Reject the change if it's trying to roll odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading. Reject the change if it's trying to pass an invalid value."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't pass a negative value.")


my_used_car = Car("subaru", "outback", 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(50)
my_used_car.read_odometer()
