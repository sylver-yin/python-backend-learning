from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace("Python", "C")
    print(line)
