banned_users = ["andrew", "sarah", "rory", "cassandra"]

user = "donna"
if user not in banned_users:
    print(f"{user.title()}, you can post a comment, if you wish.")

user = banned_users[-1]
if user not in banned_users:
    print(f"{user.title()}, you can post a comment, if you wish.")
else:
    print(f"Sorry, {user.title()}, you were banned from the comments section.")
