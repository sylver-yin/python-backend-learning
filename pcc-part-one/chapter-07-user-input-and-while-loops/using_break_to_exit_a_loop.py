prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == "quit":
        break  # NOTE: 'break' statement can be used in any of Python's loops, including 'for ... in ...:'
    else:
        print(f"I'd love to go to {city.title()}")
