print("Hello! Please, provide two numbers you want to add to each other.")

first_number = input("Please, state the first number: ")
second_number = input("Please, state the second number: ")
try:
    answer = float(first_number) + float(second_number)
except ValueError:
    print("You need to state a valid value.")
else:
    print(answer)
