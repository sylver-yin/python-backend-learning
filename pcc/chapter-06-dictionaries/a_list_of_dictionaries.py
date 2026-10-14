alien_00 = {"colour": "green", "points": "5"}
alien_01 = {"colour": "yellow", "points": "10"}
alien_02 = {"colour": "red", "points": "15"}

aliens = [alien_00, alien_01, alien_02]
for alien in aliens:
    print(alien)

zombies = []

# NOTE: range() function here tells Python how much loops we want to repeat
for zombie in range(30):
    new_zombie = {"Rarity": "Common", "HP": 100, "Speed": "Slow", "Money drop": 500}
    zombies.append(new_zombie)

for zombie in zombies[:3]:
    if zombie["Rarity"] == "Common":
        zombie["HP"] = 200
        zombie["Speed"] = "Medium"
        zombie["Money drop"] = 1000
    elif zombie["Rarity"] == "Rare":
        zombie["HP"] = 500
        zombie["Speed"] = "Fast"
        zombie["Money drop"] = 3000


for zombie in zombies[:5]:
    print(zombie)
print("...")

print(f"\nTotal number of zombies: {len(zombies)}")
