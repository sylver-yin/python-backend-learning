people_number = input("How many people is there in our group? ")
people_number = int(people_number)

if people_number >= 8:
    print(f"{people_number}?! We need to wait for a new table then!")
else:
    print("Good. Our table is just ready!")
