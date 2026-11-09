from pathlib import Path

path = Path(__file__).with_name("pi_hundred_digits.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
