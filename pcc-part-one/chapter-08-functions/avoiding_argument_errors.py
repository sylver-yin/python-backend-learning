def describe_pet(animal_type, animal_name):
    """Displays information about a pet. This one should be tried with more, fewer or even no arguments provided!"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {animal_name.title()}")


describe_pet(
    "aki", "lizard"
)  # NOTE: Also added a logical error, so the file is completely wrong. For a reference.
