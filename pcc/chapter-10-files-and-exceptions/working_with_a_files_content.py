from pathlib import Path

path = Path(__file__).with_name("pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
