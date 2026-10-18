def make_shirt(shirt_size="L", printed_message="I love Python"):
    """Showing user the t-shirt they've created."""
    print(f"\nYour t-shirt size is: {shirt_size}")
    print(f"Your printed text will be: '{printed_message}'")


make_shirt()
make_shirt("M")
make_shirt("S", printed_message="MIAMI-MIAMI-MIAMI")
