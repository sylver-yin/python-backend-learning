from module import make_pizza

make_pizza(16, "pepperoni")
make_pizza(
    32, "extra cheese", "pineapples"
)  # NOTE: It is prominent that we're not adding a 'module_name.' part there, since we explicitly state the module where it came from.

# NOTE: General syntax is 'from module_name import function_name'. We also can add as much functions as we want.
# It will look like 'from module_name import function_00, function_01, function_02' and so on.
