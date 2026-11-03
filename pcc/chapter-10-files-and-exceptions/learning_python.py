from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")
contents = path.read_text()
print(contents)

for line in contents.splitlines():
    print(line)
