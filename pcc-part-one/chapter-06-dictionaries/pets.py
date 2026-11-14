lizard_pet = {"owner": "johny", "animal": "lizard", "species": "tokay gecko"}

cat_pet = {"owner": "alice", "animal": "cat", "species": "cheshire"}

bird_pet = {"owner": "martha", "animal": "theropod", "species": "spinosaurus"}

pets = [lizard_pet, cat_pet, bird_pet]

for pet in pets:
    print(f"\nPet's owner name: {pet['owner']}")
    print(f"What animal is the pet: {pet['animal']}")
    print(f"Pet's species: {pet['species']}")
