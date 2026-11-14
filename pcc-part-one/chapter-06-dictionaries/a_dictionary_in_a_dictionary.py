users = {
    "t_ommy_2020": {
        "first name": "tommy",
        "last name": "angelo",
        "location": "lost heaven",
    },
    "wonderLis3": {
        "first name": "alice",
        "last name": "wonder",
        "location": "wonderland",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first name']} {user_info['last name']}"
    location = user_info["location"]

    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
