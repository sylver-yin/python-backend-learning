def describe_pets(pet_name, animal_type="dog"):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pets(pet_name="willie")
describe_pets(pet_name="raptor", animal_type="parrot")
describe_pets("flank")
