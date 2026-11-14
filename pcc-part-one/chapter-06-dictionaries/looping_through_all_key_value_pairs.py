user_0 = {"username": "sylver-yin", "first name": "Artem", "last name": "Sylver"}

for (
    key,
    value,
) in user_0.items():  # NOTE: Just as with lists, "key, value" are just names to assign both the key and the value.
    print(f"\nKey: {key}")
    print(f"Value: {value}")


favorite_languages = {
    "Sarah": "Python",
    "Mark": "C#",
    "Taric": "Go",
    "Tonny": "C++",
    "Ronald": "Java",
}

for name, language in favorite_languages.items():
    print(f"\n{name}'s favorite language is {language}")
