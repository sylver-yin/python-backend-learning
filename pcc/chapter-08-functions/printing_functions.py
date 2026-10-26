def print_models(unprinted_designs, completed_designs):
    """Simulates printing each 3D model and adds it to completed designs."""
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Finishing design: {current_design}\n")
        completed_designs.append(current_design)


def show_completed_models(completed_designs):
    """Displays a list of completed designs"""
    print("Completed designs:")
    for completed_design in completed_designs:
        print(f"- {completed_design}")
