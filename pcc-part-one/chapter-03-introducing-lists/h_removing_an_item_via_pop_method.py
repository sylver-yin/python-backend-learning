materials = ["wood", "metal", "leather"]
print(materials)

popped_leather = materials.pop()
print(materials)
print(popped_leather)

furniture = ["sofa", "table", "TV", "chair"]
print(furniture)
popped_furniture = furniture.pop()
print(f"The last thing you've bought was a {popped_furniture.title()}")
del furniture[2]
print(
    f"You removed {popped_furniture.title()} successfully, now the last one is {furniture[-1]}"
)  # I discovered myself that you can do this - remove 2 indexes and '-1' will show you the most recent in the list!
