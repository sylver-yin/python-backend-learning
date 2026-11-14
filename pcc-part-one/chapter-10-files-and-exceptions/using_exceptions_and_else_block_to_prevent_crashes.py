print("Give me two numbers and I'll devide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\tYou can't devide by zero!")
    else:  # NOTE: In that case, 'else' is being executed as part of 'try-except' block and depends on it! Not on 'if-else'.
        print(f"\t{answer}")
