age_string = input("How old are you? ")
age_number = int(age_string)
if age_number >= 18:
    print(f"Your age is {age_number}. Good, you're old enough to vote!")
else:
    print(
        f"Oh-oh! It looks, like your age is {age_number}! You're not old enough to vote yet."
    )

height = input("How tall are you, in centimeters? ")
height = int(height)

if height >= 125:
    print("Good, you're tall enough to ride!")
else:
    print("Sorry, you're not tall enough.")
