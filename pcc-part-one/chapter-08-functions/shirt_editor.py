def make_shirt(shirt_size="L", printed_message="I love Python"):
    """Showing user the t-shirt they've created."""
    while make_shirt:
        print(
            "Welcome to t-shirt editor! Feel free to edit the size and the print on your t-shirt! Also, type 'q' to stop."
        )
        shirt_size_ask = "Please, state your t-shirt size (L is default): "
        shirt_size = input(shirt_size_ask).strip().lower()
        if shirt_size == "q":
            break
        else:
            print(f"Your shirt size is not {shirt_size}")
        print_ask = (
            'PLease, type the message on your t-shirt ("I love Python" is default): '
        )
        printed_message = input(print_ask).lower().strip()
        if printed_message == "q":
            break
        else:
            print(f"Your message will be: {printed_message}")


# NOTE: I didn't have to make it that overcomplicated, I just decided to practice. That's the only reason.


my_shirt = make_shirt()
