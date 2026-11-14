from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path.name} has about {num_words} words.")


filenames = [
    "alice_in_wonderland.txt",
    "moby_dick.txt",
    "siddhartha.txt",
    "little_women.txt",
]
for filename in filenames:
    path = Path(__file__).with_name(filename)
    count_words(path)
