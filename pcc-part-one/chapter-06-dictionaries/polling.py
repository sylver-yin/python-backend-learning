favorite_lizards = {
    "Mike": "Tokay gecko",
    "Tonny": "Roughneck monitor",
    "Lila": "Blue tongued skink",
    "Rico": "Iguana",
}

should_participate = ["Rory", "Liam", "Rico", "Sandy", "Mike"]
for name in should_participate:
    if name in favorite_lizards:
        print(f"{name.title()}, thank you for participating!")
    else:
        print(f"Please, {name.title()}, consider to participate in the poll!")
