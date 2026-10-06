my_favorite_colours = ["red", "pink", "green"]
friend_favorite_colours = my_favorite_colours[:]

my_favorite_colours.append("purpule")
friend_favorite_colours.append("brown")

print("\nHere are my favorite colours:")
for my_colour in my_favorite_colours:
    print(my_colour)

print("\nHere are my friend's favorite colours:")
for friend_colour in friend_favorite_colours:
    print(friend_colour)

print("\n\tSpot the difference!")
