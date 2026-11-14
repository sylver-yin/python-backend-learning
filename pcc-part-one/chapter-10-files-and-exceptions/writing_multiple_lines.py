from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also like working with data.\n"

path = Path(
    "D:/python-backend-learning/pcc/chapter-10-files-and-exceptions/programming.txt"
)
path.write_text(contents)
