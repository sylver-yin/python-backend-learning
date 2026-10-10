requested_toppings = ["pepperoni", "extra cheese", "mushrooms"]

for requested_topping in requested_toppings:
    if requested_topping == "mushrooms":
        print("Sorry, we ran out of mushrooms")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")
