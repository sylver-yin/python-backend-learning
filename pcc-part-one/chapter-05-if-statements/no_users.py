users = ["Crhis", "admin", "Roland", "Tracy", "Tom"]

if users:
    for username in users:
        if username == "admin":
            print("Hello, Admin, would you like to see reports?")
        else:
            print(f"Hello, {username}, thank you for loggining.")
else:
    print("No one loggined in.")


users_empty = []  # EXPLANATION: It will be same if else, to make sure it works propperly without deleting elements.

if users_empty:
    for no_ones in users_empty:
        if username == "admin":
            print("Hello, Admin, would you like to see reports?")
        else:
            print(f"Hello, {no_ones}, thank you for loggining.")
else:
    print("No one logged in.")
