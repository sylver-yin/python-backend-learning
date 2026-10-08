my_foods = ["Mac 'n Cheese", "Pizza", "Soda"]
friend_foods = my_foods[:]

my_foods.append("Chocolate")
friend_foods.append("Carrot")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# TIP: A slice creates a copy of the list, while assigning one variable to another makes both variables refer to the same list
