sandwich_orders = [
    "blt sandwich",
    "pastrami",
    "club sandwich",
    "pastrami",
    "reuben sandwich",
    "philly cheesesteak sandwich",
    "pastrami",
]
finished_sandwiches = []

print("Sorry, we ran out of Pastrami!")

while sandwich_orders:
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")

    current_sandwich = sandwich_orders.pop()
    print(f"Finished doing your {current_sandwich}!")
    finished_sandwiches.append(current_sandwich)


print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
