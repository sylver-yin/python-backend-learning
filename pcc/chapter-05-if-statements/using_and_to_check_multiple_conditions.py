age_00 = 22
age_01 = 18
if age_00 >= 21 and age_01 >= 21:
    print("True")
else:
    print("False")

age_01 = 22
if (age_00 >= 21) and (
    age_01 >= 21
):  # It shown that parentheses are not required bur can improve readability.
    print("True")
else:
    print("False")
