peoples_numbers = {
    "sarah": [91, 82, 77],
    "john": [99, 25, 24, 11],
    "chris": [10, 1, 3, 4, 9],
    "taric": [4, 95, 20000],
    "july": [1, 20, 33],
}

for name, numbers in peoples_numbers.items():
    print(f"\n{name.title()} favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
