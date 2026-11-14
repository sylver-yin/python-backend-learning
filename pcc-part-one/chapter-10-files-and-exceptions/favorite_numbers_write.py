import json
from pathlib import Path

favorite_numbers = []
path = Path(__file__).with_name("favorite_numbers.json")
while True:
    user_number = (
        input('Please, state your favorite numbers! Type "s" to stop. ').lower().strip()
    )
    try:
        if user_number == "s":
            contents = json.dumps(favorite_numbers)
            path.write_text(contents)
            break
        else:
            favorite_numbers.append(float(user_number))
            continue
    except ValueError:
        print("Please, state a number.")
