name_input = input("Please, tell me your name: ")
name = name_input.title()
print(f"Hello, {name}")

prompt = "If you share your age, we can personalize the messages you see."
prompt += "\nHow old are you? "  # NOTE: In this example += doesn't really matter, so putting them in one string would be better here.

age = input(prompt)
print(f"Your age is {age}! Thank you for sharing your information for the poll.")
