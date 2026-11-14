print("Hello, type any two numbers that you want to add in this calculator.")
print("Type 'q' at any time to exit.")


while True:
    first_value = input("Please, state the first value: ").lower().strip()
    if first_value == "q":
        break
    second_value = input("Please, state the second value: ").lower().strip()
    if second_value == "q":
        break
    try:
        answer = float(first_value) + float(second_value)
    except ValueError:
        print(
            "\tIt seems one or both of the stated values are not valid. Please, try again."
        )
    else:
        print(f"\t{answer}")
