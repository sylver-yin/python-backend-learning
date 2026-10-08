square_numbers = []
for value in range(2, 11):
    square = value**2
    square_numbers.append(square)

print(square_numbers)

# Tip: there are two methods. Both should work. ^^^UPPER^^^ and vvvLOWERvvv work the same:

squares = []
for number in range(2, 11):
    squares.append(number**2)

print(squares)
