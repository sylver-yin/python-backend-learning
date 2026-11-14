from pathlib import Path

path = Path(__file__).with_name("alice_in_wonderland.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, file '{path}' was not found")
else:
    words = contents.split()
    num_word = len(words)
    print(f"The file '{path}' has about {num_word} words.")
