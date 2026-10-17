responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhat is your favorite pizza? ")
    responses[name] = response  # NOTE: That's how we store response in a dictionary.

    repeat = input("\nWould you like to let next person respond (yes/no)? ")
    if repeat == "no":
        polling_active = False

print("\n=== POLL RESULTS ===")
for name, response in responses.items():
    print(f"{name.title()}'s favorite pizza is {response.title()}")
