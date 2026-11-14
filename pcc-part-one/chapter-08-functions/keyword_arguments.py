def describe_pets(anima_type, animal_name):
    """Displays information about a pet."""
    print(f"\nI have a {anima_type}")
    print(f"My {anima_type}'s name is {animal_name.title()}")


describe_pets(anima_type="dog", animal_name="lana")
describe_pets(animal_name="harry", anima_type="hamster")
