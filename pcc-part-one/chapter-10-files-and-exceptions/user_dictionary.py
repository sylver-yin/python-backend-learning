import json
from pathlib import Path


def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text(encoding="utf-8")
        user_info = json.loads(contents)
        return user_info
    else:
        return None


def ask_user_info(path):
    while True:
        try:
            username = input("Please, state your name: ").lower().strip()
            user_age = input("Please, state your age: ").strip()
            user_country = input("Please, state your country: ").lower().strip()
            user = {
                "Username": username,
                "User's age": int(user_age),
                "User's country": user_country,
            }
            contents = json.dumps(user)
            path.write_text(contents, encoding="utf-8")
            break
        except ValueError:
            print("Please, state valid age!")
            continue
    return user


def greet_user():
    path = Path(__file__).with_name("user_info.json")
    user_info = get_stored_user_info(path)
    if user_info:
        print(
            f"Hello! You are {user_info['Username'].title()}, you're {user_info["User's age"]}, you're from {user_info["User's country"].title()}"
        )
    else:
        user_info = ask_user_info(path)
        print("Thank you! We will remember your data:")
        for key, value in user_info.items():
            print(f"{key}: {value}")


greet_user()
