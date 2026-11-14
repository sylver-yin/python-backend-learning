users = ["Crhis", "admin", "Roland", "Tracy", "Tom"]

for username in users:
    if username == "admin":
        print("Hello, Admin, would you like to see a status report?")
    else:
        print(f"Hello, {username.title()}, thank for you logging in again.")
