def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("hamster", "jerry")
describe_pet("dog", "lana")
describe_pet(
    "raptor", "parrot"
)  # NOTE: This is how possible logical error looks like. Code is working but the result is wrong.
