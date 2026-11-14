current_users = ["jOhn", "Sarah", "alICe", "ToNnY", "mARIE"]
user_lower = []

new_users = ["John", "ChrIS", "Lilly", "AliCe", "Rory"]

for user_original in current_users:
    lowercase_check = user_original.lower()
    user_lower.append(lowercase_check)
print(user_lower)

for usernames in new_users:
    if usernames.lower() in user_lower:
        print("Sorry, this name is already taken.")
    else:
        print("You have registred succesfully.")
