import json
from pathlib import Path

path = Path(__file__).with_name("username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username.title()}!")
