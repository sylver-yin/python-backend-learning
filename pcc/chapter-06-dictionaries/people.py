person_00 = {"first name": "Vlad", "last name": "Kozak", "age": 20, "city": "Dnipro"}

person_01 = {
    "first name": "Anastasija",
    "last name": "Kirova",
    "age": 56,
    "city": "Cherkasy",
}

person_02 = {
    "first name": "Vladyslava",
    "last name": "Vizor",
    "age": 56,
    "city": "Kyiv",
}

people = [person_00, person_01, person_02]

for person in people:
    print(f"\nFirst name: {person['first name']}")
    print(f"Last name: {person['last name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
