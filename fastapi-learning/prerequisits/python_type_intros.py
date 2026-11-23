def get_full_name(
    first_name: str, last_name: str
):  # <- Those are called "type hints", they're letting us to specify the data type.
    full_name = (
        first_name.title() + " " + last_name.title()
    )  # NOTE: Just to show that I can do that.
    return full_name


print(get_full_name("Vlad", "Mercury"))


def get_name_with_age(name: str, age: int):
    name_with_age = f"{name.title()} is this old: {str(age)}."  # noqa: RUF010
    return name_with_age


print(get_name_with_age("alex", 19))


def get_items(
    item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes
):  # You can use type hints with every standard Python data type.
    return item_a, item_b, item_c, item_d, item_e
