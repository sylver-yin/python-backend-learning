from pathlib import Path


def read_contents(path):
    """Read the contents of the file provided."""
    print(f"\nHere is the contents of '{path.name}':")
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file '{path.name}' was not found.")
    else:
        for name in contents.splitlines():
            print(f"\t{name}")


dogs = Path(__file__).with_name("dogs.txt")
read_contents(dogs)
cats = Path(__file__).with_name("cats.txt")
read_contents(cats)
