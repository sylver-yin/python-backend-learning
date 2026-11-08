import json
from pathlib import Path

path = Path(__file__).with_name("favorite_numbers.json")
if path.exists():
    contents = path.read_text()
    favorite_numbers = json.loads(contents)
    if len(favorite_numbers) == 1:
        print(f"I know your favorite numbers is: {favorite_numbers}")
    else:
        print(f"I know your favorite numbers are: {favorite_numbers}")
else:
    print("Sorry, state your favorite numbers first!")
