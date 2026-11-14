def build_character(name, character_class, age=None, level=1):
    """Return a dictionary with user's character."""
    character = {"name": name, "class": character_class, "level": level}
    if age:
        character["age"] = age
    return character


player = build_character("Ralof", "Barbarian", 33)
print(player)
player = build_character("Mina", "Mage", 592, 3)
print(player)
