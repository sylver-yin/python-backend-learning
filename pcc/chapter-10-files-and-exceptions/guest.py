from pathlib import Path

path = Path("D:/python-backend-learning/pcc/chapter-10-files-and-exceptions/guest.txt")
full_name = input("Please, state your first and last name: ").title()
path.write_text(full_name)
