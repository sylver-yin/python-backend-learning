def greet_users(names):
    """Writes a simple greeting to each user in the list."""
    for name in names:
        message = f"Hello, {name.title()}"
        print(message)


usernames = ["rory", "sarah", "tonny"]
greet_users(usernames)
