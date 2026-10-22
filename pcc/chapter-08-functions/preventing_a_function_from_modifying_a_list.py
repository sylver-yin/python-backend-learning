def print_models(unprinted_designs, completed_designs):
    """Simulates printing each design, until none are left. Move each design to completed_prints after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Printing model: {current_design}")
        completed_designs.append(current_design)


def show_completed_designs(completed_designs):
    """Show all models that were printed."""
    print("\nThe following designs have been printed:")
    for completed_design in completed_designs:
        print(completed_design)


unprinted_designs = ["ring", "mini figure", "gear"]
completed_designs = []

print_models(unprinted_designs[:], completed_designs)
show_completed_designs(completed_designs)

# NOTE: It's just immitates the process to show that we can use slices to make an intact copy if we don't want to change the original list.
