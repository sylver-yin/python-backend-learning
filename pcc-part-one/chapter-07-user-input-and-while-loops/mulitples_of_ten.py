number = input("Give me the number and I will say if it's a multiple of ten or not: ")
number = int(number)

if number % 10 == 0:
    print("It's a multiple of ten.")
else:
    print("It's not multiple of ten.")
