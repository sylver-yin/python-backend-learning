from pathlib import Path

path = Path(
    "D:/python-backend-learning/pcc/chapter-10-files-and-exceptions/guest_book.txt"
)


def get_full_name():
    """Ask user for their full name and return it neatly organised."""
    first_name = input("Please, provide your firstname: ").lower().strip()
    last_name = input("Please, provide your lastname: ").lower().strip()
    full_name = f"{first_name} {last_name}\n"
    return full_name.title()


names = ""
print("Hello, guests. I want you to state your full name if you will go to the party.")
while True:
    ask_for_quit = (
        (input("You want to add your name? Type 'y' to keep adding and 'n' to quit: "))
        .strip()
        .lower()
    )
    if ask_for_quit == "n":
        path.write_text(names)
        break
    elif ask_for_quit == "y":
        names += get_full_name()
