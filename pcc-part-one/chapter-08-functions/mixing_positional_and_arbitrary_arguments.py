def make_pizza(size, *toppings):
    """Prints a size of pizza and the list of toppings that have been requested."""
    print(f"\nMaking a {size}-cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(30, "cheese", "pineapples")
