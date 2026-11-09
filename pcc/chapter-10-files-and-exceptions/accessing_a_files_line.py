from pathlib import Path

path = Path(__file__).with_name("pi_digits.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)
