import json
from pathlib import Path

numbers = [1, 3, 7, 9, 11, 13]

path = Path(__file__).with_name("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
