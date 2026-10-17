sandwich_orders = [
    "blt sandwich",
    "club sandwich",
    "reuben sandwich",
    "philly cheesesteak sandwich",
]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"\nFinished making your {current_sandwich}!")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
