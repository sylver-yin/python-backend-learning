alien_00 = {"colour": "green", "points": 5}
print(f"The alien is {alien_00['colour']}")

alien_00["colour"] = "yellow"
print(f"The alien is now {alien_00['colour']}!")

alien_01 = {"x_position": 0, "y_position": 25, "speed": "slow"}
print(f"Original position: {alien_01['x_position']}")

if alien_01["speed"] == "slow":
    x_increment = 1
elif alien_01["speed"] == "medium":
    x_increment = 2
else:  # NOTE: Imo, "elif alien_01["'speed'] == 'fast'" would be much better if we have more than 3 speed modes or it's dynamic.
    x_increment = 3

alien_01["x_position"] = alien_01["x_position"] + x_increment

print(f"New position is {alien_01['x_position']}")
