import json
from pathlib import Path


def get_stored_numbers(path):
    if path.exists():
        contents = path.read_text()
        favorite_numbers = json.loads(contents)
        return favorite_numbers
    else:
        return None


def ask_for_numbers(path):
    added_numbers = []
    while True:
        user_number = (
            input(
                'Type "s" to stop. Please, state your favorite numbers (one per write): '
            )
            .lower()
            .strip()
        )
        if user_number == "s":
            contents = json.dumps(added_numbers)
            path.write_text(contents)
            break
        else:
            added_numbers.append(float(user_number))


def show_favorite_numbers():
    path = Path(__file__).with_name("favorite_numbers.json")
    favorite_numbers = get_stored_numbers(path)
    if favorite_numbers:
        if len(favorite_numbers) == 1:
            print(f"Your favorite number is: {favorite_numbers[0]}")
        else:
            print("Your favorite numbers are:")
            for number in favorite_numbers:
                print(f"\t{number}")
    else:
        favorite_numbers = ask_for_numbers(path)
        print("Your favorite numbers were saved!")


show_favorite_numbers()
