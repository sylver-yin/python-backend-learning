def make_pizza(*toppings):
    """Prints a list of toppings that have been requested."""
    print("\nMaking a pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("pepperoni")
make_pizza("cheese", "pepperoni", "pineapples")
