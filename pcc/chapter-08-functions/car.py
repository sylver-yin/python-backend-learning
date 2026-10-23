def get_car_info(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info


car = get_car_info("audi", "a3 sedan", color="red", fuel="petrol")

print(car)
