from pathlib import Path

path = Path(__file__).with_name("alice.txt")
try:
    contents = path.read_text(encoding="utf=8")
except FileNotFoundError:
    print(f'Sorry, the file "{path}" was not found.')
