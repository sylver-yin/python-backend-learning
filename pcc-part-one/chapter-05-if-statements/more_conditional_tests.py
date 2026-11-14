geckos = ["crested gecko", "leopard gecko", "day gecko"]
for gecko in geckos:
    if gecko == "crested gecko":
        print("It's a crestie! True.")
    else:
        print("Not a crestie! False.")
    if gecko != "day gecko":
        print("Not a day gecko! True")
    else:
        print("It's a day gecko! False")

car = "BMW"
print(car.lower() == "bmw")

age = 18
if age == 18:
    print("You're 18, you can marry.")
else:
    print("You're under 18, you can't marry.")
if age != 18:
    print("This product suits you.")
else:
    print("This product does not suits you.")
if age > 20:
    print("Since you're 21 - you're able to buy alcohol.")
else:
    print(
        "Sorry, you're less than 21, you still can't buy alcohol, but you're legal adult citizen."
    )
if age < 18:
    print("We can't allow you to enter this website.")
else:
    print("We can allow you enter this website.")
if age >= 18:
    print("You are the part of 18-24 year old auditory of this channel.")
else:
    print("You are part of different age auditory. Want to change it?")
if age <= 18:
    print("Sorry, but we can't sell alcohol to people under 21, even if you're 18.")
else:
    print("We can sell this product to you, sir. Here's your receipt")

answer_00 = 45
answer_01 = 90
if (answer_00 == 45) and (answer_01 < 50):
    print("You have passed the test!")
else:
    print("You have not passed the test!")

age_01 = 18
age_02 = 21
if (age_01 >= 18) or (age_02 >= 18):
    print("True, at least one adult")
else:
    print("False, no adults.")

colours = ["Red", "Orange", "Purpule", "Green", "White"]
favourite_colour = "Purpule"

if favourite_colour in colours:
    print("We have your favourite one!")
else:
    print("Sorry, we don't have the one you like the most.")

pepperoni_ingredients = ["Dough", "Cheese", "Ketchup", "Sausages"]
dislike = "Tomatoes"

if dislike not in pepperoni_ingredients:
    print("No need to worry, we don't have it!")
else:
    print("Okay, we do have it, but we can remove it in no time!")
