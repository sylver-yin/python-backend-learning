age = input(
    "Ticket prices: \n\tUnder 3 - $0; \n\tUnder 12 - $10; \n\t12 and older - $15; \nPlease, enter your full age with numbers: "
)
age = int(age)


if age < 0:
    print("Please, state valid age.")
elif age < 3:
    print("Age setted. Your ticket price is $0")
elif age < 12:
    print("Age setted. Your ticket price is $10")
else:
    print("Age setted. Your ticket price is $15")
