unprinted_designs = ["phone case", "robot pedant", "dodecahedron"]
completed_models = []

# NOTE: We pretend that each design is being printed and none are left. Now we moving it to another list.

while unprinted_designs:
    current_design = unprinted_designs[
        0
    ]  # NOTE: In the book we made it with .pop() method and without del statement. I just wanted to test it.
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    del unprinted_designs[0]

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# NOTE: This ^ is how it would look without a function! And this v is how it will look with a function:


def print_models(unprinted_models, completed_prints):
    """Simulates printing each design, until none are left. Move each design to completed_prints after printing."""
    while unprinted_models:
        current_order = unprinted_models.pop()
        print(f"Printing: {current_order}")
        completed_prints.append(current_order)


def show_completed_models(completed_prints):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_prints:
        print(completed_model)


unprinted_models = ["mini figure", "cube", "ring"]
completed_prints = []

print_models(
    unprinted_models=unprinted_models, completed_prints=completed_prints
)  # NOTE: Key arguments here are redundunt, it's just a practice to remember they exist!
show_completed_models(completed_prints)
