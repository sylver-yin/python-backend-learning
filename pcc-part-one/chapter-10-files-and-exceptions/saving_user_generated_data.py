import json
from pathlib import Path

username = input("What is your name? ")

path = Path(__file__).with_name("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember you when you come back, {username.title()}!")
