favorite_games = {
    "Jack": "Metal Gear Solid",
    "Rory": "Monster Hunter World",
    "Nathan": "Outer Wilds",
    "Rosa": "League of Legends",
    "Lilly": "League of Legends",
}

print("The following games have been mentioned (with repeats):")
for game in favorite_games.values():
    print(game.title())

print("\nThe following games have been mentioned (without repeats):")
for game_unique in set(favorite_games.values()):
    print(game_unique.title())

print(favorite_games)
# NOTE: "set()" is the collection in which every item must be unique. However it is not deleting any values nor changing them.
