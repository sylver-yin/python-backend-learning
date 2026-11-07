from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(
            f"Sorry, the file '{path.name}' was not found."
        )  # NOTE: I found out how to show only the file name without the whole path in output! I can use {filename}.name method.
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file '{path.name}' has about {num_words} words in it.")


path = Path(__file__).with_name("alice_in_wonderland.txt")
count_words(path)

filesnames = [
    "alice_in_wonderland.txt",
    "moby_dick.txt",
    "little_women.txt",
    "siddhartha.txt",
]  # NOTE: We intentionally add the non existing file so we can see if 'try-except-else' works correctly.
for filename in filesnames:
    path = Path(__file__).with_name(f"{filename}")
    count_words(path)
