class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Intisalise info about the car that is provided by user."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Provides a neatly organised name of a car in the YEAR-MAKE-MODEL order."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Provides the reading from car's odometer."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer_value(self, mileage):
        """Sets odometer reading to the provided value. Rejects the rollback operations."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback the odometer.")

    def increment_odometer_value(self, added_miles):
        """Increments the odometer value by a provided number. Rejects negative numbers."""
        if added_miles >= 0:
            self.odometer_reading += added_miles

    def fill_gas_tank(self):
        """Prints statement about gas tank being filled."""
        print("Gas tank is being filled...")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Prints a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """A simple attempt to represent the variation of car class by making an electric car."""

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class. Then initialise attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Prints a statement that is rejecting user because electric cars don't use gas."""
        print("This car doesn't have a gas tank.")


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
