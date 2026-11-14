from pathlib import Path


def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
        the_count = contents.lower().count("the")
        print(f"\nIn '{path.name}' the word 'the' appears around {the_count} times")
        the_space_count = contents.lower().count("the ")
        print(
            f"In '{path.name}' the word 'the ' (with space) appears around {the_space_count} times."
        )
    except FileNotFoundError:
        print(f"Sorry, the file '{path.name}' was not found.")


dracula = Path(__file__).with_name("dracula.txt")
count_words(dracula)

ivanhoe = Path(__file__).with_name("ivanhoe.txt")
count_words(ivanhoe)
