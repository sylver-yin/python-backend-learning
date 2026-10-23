def make_sandwich(*ingredients):
    """Displays an ingredients that user requested for their sandwich."""
    print("\nAdding next ingredients to your sandwich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich("ham")
make_sandwich("ham", "cheese")
make_sandwich("salad", "ham", "cheese")


# NOTE: VVV This one VVV is not requested in Try yourself. I did it for fun!! I didn't even knew about it yet, it's page 149


def accept_user_toppings(toppings):
    """Test to see if I can put input there!"""
    while True:
        topping = "\nPlease, type the topping you want to put on your pizza."
        topping += "\n(type 'q' to exit at any time and see your requests) "

        message = input(topping).lower().strip()
        if message == "q":
            print(toppings)
            break
        else:
            if message in topping_in_stock:
                print(f"Adding {message} to your pizza")
                toppings.append(message)
            else:
                print(
                    "Looks like topping you're trying to add is not in stock. Try again."
                )


topping_in_stock = ["cheese", "pepperoni", "mushrooms"]
client_request = []

accept_user_toppings(client_request)


guest_list = []
new_guest = input("guest")

guest_list.append(new_guest)
