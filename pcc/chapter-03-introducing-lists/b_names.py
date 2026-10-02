friends_names = ["vladyslav", "DMYTRO", "OlEg"]
print(friends_names[0].title())
print(friends_names[1].title())
print(friends_names[2].title())

user_penalty_00 = (
    f"Hello, {friends_names[0].title()}, your account was suspended due to inactive."
)
user_pentaly_01 = (
    f"Hello, {friends_names[1].title()}, your account was suspended due to inactive."
)
user_penalty_02 = (
    f"Hello, {friends_names[2].title()}, your account was suspended due to inactive."
)
print(user_penalty_00, user_pentaly_01, user_penalty_02)
