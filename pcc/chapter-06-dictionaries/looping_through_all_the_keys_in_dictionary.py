favorite_lizards = {
    "Mike": "Tokay gecko",
    "Tonny": "Roughneck monitor",
    "Lila": "Blue tongued skink",
    "Rico": "Iguana",
}

friends = ["Mike", "Rico"]
for name in favorite_lizards.keys():  # noqa: PLC0206, SIM118
    print(f"Hi, {name.title()}.")
    # NOTE: Looping through the keys is basic behavior for looping through the dictionary, so code will work even without ".keys()" method

    if name in friends:
        lizard = favorite_lizards[name].title()
        print(f"\t{name.title()}, I see you love {lizard}")

if "Clyde" not in favorite_lizards:
    print("Clyde please tell about your lizards!")
