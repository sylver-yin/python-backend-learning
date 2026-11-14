def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a fullname, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


worker = get_formatted_name("samuel", "hiden", "chris")
print(worker)
worker = get_formatted_name("Maria", "crush")
print(worker)
