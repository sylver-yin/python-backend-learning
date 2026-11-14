import json
from pathlib import Path

path = Path(__file__).with_name("user_real_name.json")
if path.exists():
    contents = path.read_text()
    user_real_name = json.loads(contents)
    print(f"Hi, {user_real_name.title()}!")
else:
    user_real_name = input("Please, state your real name: ")
    contents = json.dumps(user_real_name)
    path.write_text(contents)
    print(f"We will remember you next time you come back, {user_real_name.title()}!")
