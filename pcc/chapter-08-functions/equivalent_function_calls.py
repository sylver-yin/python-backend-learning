def describe_pet(pet_name, animal_type="dog"):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


# NOTE: Ways to use function calls differently:
describe_pet("willie")
describe_pet(pet_name="nida")
describe_pet(
    animal_type="dog", pet_name="lana"
)  # NOTE: This one is redundunt but still usable if needed.

describe_pet("harry", "hamster")
describe_pet(pet_name="raptor", animal_type="parrot")
describe_pet(animal_type="lizard", pet_name="aki")
