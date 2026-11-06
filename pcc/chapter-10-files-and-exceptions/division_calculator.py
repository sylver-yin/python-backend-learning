print("Give me two numbers and I'll devide them")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ").strip().lower()
    if first_number == "q":
        break
    second_number = input("\nSecond number: ").strip().lower()
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# NOTE: Obviously, it will raise an error if we use as the second number 0, but except block will be later so I will leave it like this.
