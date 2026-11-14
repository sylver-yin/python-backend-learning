def send_messages(unsent_messages, sent_messages):
    """Simulates sending messages and adds messages from unsent list to sent list."""
    while unsent_messages:
        current_message = unsent_messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)


def show_lists_state(unsent_messages, sent_messages):
    """Shows the lists state at the moment."""
    print(f"\nThe lists now: \nUnsent: {unsent_messages}, Sent: {sent_messages}\n")


unsent_messages = ["Lol!", "spooky!", "2+2=5", "MARIA."]
sent_messages = []

show_lists_state(unsent_messages, sent_messages)
send_messages(unsent_messages, sent_messages)
show_lists_state(unsent_messages, sent_messages)
