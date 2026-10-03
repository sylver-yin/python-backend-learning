list = []  # If you'll try to ask for [-1] index in an empty list - you would get a syntax error "List index out of range".
print("\nYour list is empty for now!")
print(list)

list.insert(0, "Pencil")
list.append("Fish")
print(f"\n{list[0]}, {list[1]} had been added to your grocceries list!")
print(list)

list.insert(2, "Water")
print(f"\n{list[2]} had been added to your grocceries list!")
print(list)

list_new_01 = "Carrot"
print(f"\n{list[2]} has been changed to {list_new_01}")
list[2] = f"{list_new_01}"
print(list)

list_popped = list.pop()
print(f"\n{list_popped} was removed!")
print(list)

print(f"\n{list[0]} was removed!")
del list[0]
print(list)

list.append("Soda")
print(f"\n{list[1]} had been added to your grocceries list!")
print(list)

print("\nNot enough money. Please, delete something from your cart:")
print(list)
print(f"{list[1]} was removed!")
too_expensive = list[1]
list.remove(too_expensive)

print("\nHere's your list:")
print(list)
print("List lenght:", len(list))
