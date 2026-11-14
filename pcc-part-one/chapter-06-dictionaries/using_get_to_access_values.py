alien_00 = {"colour": "green", "speed": "slow"}

point_value = alien_00.get("points", "No point value assigned")
print(point_value)

# NOTE: If no second argument assigned, Python will return "None". It's not an error, it's a special value. Here's the example
x_position = alien_00.get("x_position")
print(x_position)
