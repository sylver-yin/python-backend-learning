from name_function import get_formatted_name

print("Type 'q' at any time to end programm.")
while True:
    first = input("Please, state your first name: ").lower().strip()
    if first == "q":
        break
    middle = (
        input("If you have a middle name, state it here. If not, reamin blank: ")
        .lower()
        .strip()
    )
    if middle == "q":
        break
    last = input("Please, state your last name: ").lower().strip()
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\tHere's your neatly formatted name: {formatted_name}.")
