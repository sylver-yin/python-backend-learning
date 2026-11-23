# 1. List:


def process_items_01(
    items: list[str],
):  # NOTE: Data type in brackets are called 'type parameters', which we pass to the data type outside of them.
    for item in items:
        print(item)


process_items_01(["Tomato", "Banana"])

# 2. Tuple and set:


def process_items_02(item_t: tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s


# 3. Dictionary:


def process_items_03(prices: dict[str, float]):
    for product, cost in prices.items():
        print(f"{product}\t${cost}")


process_items_03(
    {"banana": 10.33, "tomato": 3.99}
)  # You need to pass a dict for this function.


# 4. Union:


def process_items_04(
    item: str | int,
):  # NOTE: We use "a | b" syntax for union. Union means that item could be a or b.
    print(item)


process_items_04(3)


# 5. Possibly None:


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hello, {name.title()}!")
    else:
        print("Hello World!")


say_hi()


# 6. Classes as types:


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name.title()


person = Person("eli")
print(get_person_name(person))
