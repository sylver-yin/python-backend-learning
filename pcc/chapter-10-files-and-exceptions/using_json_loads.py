import json
from pathlib import Path

path = Path(__file__).with_name("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
