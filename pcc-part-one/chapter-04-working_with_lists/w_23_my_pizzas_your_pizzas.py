my_pizzas = ["Pepperoni pizza", "Sea food pizza", "Four cheese pizza"]
friend_pizzas = my_pizzas[:]

print("\nHere are my favorite pizzas:")
for my_pizzas_before in my_pizzas:
    print(f"{my_pizzas_before}")

print("\nHere are my friend's favorite pizzas:")
for friend_pizzas_before in friend_pizzas:
    print(f"{friend_pizzas_before}")

my_pizzas.append("Pineapple pizza")
friend_pizzas.append("Hunter pizza")

print("\nHere are my favorite pizzas now:")
for my_pizzas_after in my_pizzas:
    print(f"{my_pizzas_after}")

print("\nHere are my friend's favorite pizza now:")
for friend_pizzas_after in friend_pizzas:
    print(f"{friend_pizzas_after}")

print("\nWe are not the same!")
