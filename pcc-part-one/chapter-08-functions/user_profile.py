def get_user_info(first, last, **userinfo):
    userinfo["first name"] = first
    userinfo["last name"] = last
    return userinfo


user_profile = get_user_info(
    "artem", "shepshelej", age=19, favorite_game="Outer Wilds", status="student"
)

print(user_profile)
