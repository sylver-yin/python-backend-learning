import json
from pathlib import Path


def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Greet user by name or promptt to give it if no file with name was found."""
    path = Path(__file__).with_name("username.json")
    username = get_stored_username(path)
    user_verification = input(f"Hello! Are you {username}? Y/N: ").lower().strip()
    if username:
        if user_verification == "y":
            print(f"Welcome back, {username.title()}")
        elif user_verification == "n":
            username = get_new_username(path)
            print(f"Thank you for providing new data, {username.title()}!")
    else:
        username = get_new_username(path)
        print(f"We will remember you once you come back, {username.title()}!")


greet_user()
