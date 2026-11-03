from pathlib import Path

path = Path(
    __file__
).with_name(
    "pi_digits.txt"
)  # NOTE: Since it's not Python working directory, I need to use (__file__).with_name('...') in these situations.
contents = path.read_text().strip()
print(contents)
# NOTE: Also, in this situation (__file__).with_name used as a relative file path.
