def make_shirt(shirt_size, printed_text):
    """Showing user the t-shirt they've created."""
    print(f"\nYour t-shirt size is: {shirt_size}")
    print(f"Your printed text will be: '{printed_text}'")


make_shirt("XL", "Big boss, small cortizol")
make_shirt(shirt_size="L", printed_text="I <3 CANADA")
make_shirt(printed_text="What is a shower?", shirt_size="M")
