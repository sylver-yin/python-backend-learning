prompt = (
    "\nPlease, write down any toppings for the pizza you would like to have one by one."
)
prompt += (
    "\nEnter 'quit' if you have finished or 'change' to get back to pizza select. "
)

active = True
client_choice = ""
while active:
    client_choice = input(prompt)

    if client_choice == "change":
        print("Here, take a look at our pizzas again")
        active = False
    elif client_choice == "quit":
        break
    elif client_choice != "quit":
        print(f"Adding {client_choice} to the toppings!")
