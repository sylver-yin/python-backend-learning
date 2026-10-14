pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}

print(f"You ordered {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")

favorite_languages = {
    "jane": ["python", "java"],
    "max": ["c++", "go"],
    "rory": ["c#", "python"],
    "alice": ["rust"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")
