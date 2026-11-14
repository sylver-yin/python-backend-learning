message = "Hello, Python!"
print(message)  # If you press TAB here you will indent the call,
# Which won't work and result a "IndentationError" syntax error. Simply, don't use indent when it's not mandatory.

colon_forgot_example = ["meat", "fish", "greens"]
for example in colon_forgot_example:
    print(
        f"If you will forget the colon after 'in' statement, \nThe loop simply won't work! Bye-bye, {example.upper()}!"
    )
# And also you'll get "SyntaxError: expected ':'". It's easy to fix, but it maybe not that easy to notice!
