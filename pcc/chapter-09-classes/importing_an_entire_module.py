import car

my_car = car.Car("audi", "a4", 2024)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_leaf = car.ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
