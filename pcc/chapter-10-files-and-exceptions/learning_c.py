from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")
contents = path.read_text().replace("Python", "C")

lines = contents.splitlines()
for line in lines:
    print(line)
