prompt = (
    "\nPlease, write down any toppings for the pizza you would like to have one by one."
)
prompt += "\nEnter 'quit' if you have finished. "

client_choice = ""
while client_choice != "quit":
    client_choice = input(prompt)

    if client_choice != "quit":
        print(f"We added {client_choice.title()} succesfully!")

# NOTE: It's not real toppings adding script, just while loop check.
