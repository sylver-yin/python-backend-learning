prompt = "\nHi, I'm Parrot! Type something - and I will repeat!"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
