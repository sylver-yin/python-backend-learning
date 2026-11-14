print("\tPython")

print("Groceries:\nSalad\nSalmon\nCheese")

print("\n\tYou\n\tShould\n\tEat\n\tYour\n\tGreens!")

print("\nFear\n\tThe\n\t\tPython\n\t\t\tSnake!")

favorite_lizard = "Iguana "
favorite_lizard = favorite_lizard.rstrip()
print(favorite_lizard)

hated_fish = " Salmon"
hated_fish = hated_fish.lstrip()
print(hated_fish)

lucky_number = " 25 "
lucky_number = lucky_number.strip()
print(lucky_number)

youtube_url = "https://www.youtube.com"
youtube_url = youtube_url.removeprefix("https://")
print(youtube_url)

simple_url = youtube_url.removeprefix("https://")
print(simple_url)

cat = "scarylarry"  # You don't need no spaces in between text, the removeprefix method works fine.
cat = cat.removeprefix("scary")
print(cat)
