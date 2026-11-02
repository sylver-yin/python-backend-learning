from car import Car
from electric_car import ElectricCar as electric_car

my_car = Car("audi", "a4", 2024)
print(my_car.get_descriptive_name())

my_leaf = electric_car("nissan", "leaf", 2020)
print(my_leaf.get_descriptive_name())
