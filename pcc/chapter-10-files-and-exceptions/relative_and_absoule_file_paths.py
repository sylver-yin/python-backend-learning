from pathlib import Path

# NOTE: This vvv is called an absoulte file path. It tells exactly where the file is.
path = Path(
    "D:/python-backend-learning/pcc/chapter-10-files-and-exceptions/text-files/pi_digits_inside.txt"
)  # NOTE: If we shorten it to 'chapter-10-files-and-exceptions/pi_digits.txt' it will be a relative path. However sometimes it doesn't work.
contents = path.read_text().strip()
print(contents)

path = Path(
    __file__
).with_name(
    "pi_digits.txt"
)  # NOTE: In this case we use (__file__).with_name('...') as relative file path since it's not Python working directory.
contents = path.read_text().strip()
print(contents)
