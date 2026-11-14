from module import *

make_pizza(16, "pepperoni")
make_pizza(32, "green peppers", "extra cheese")

# NOTE: General syntax is 'from module_name import *'. However, it's not the best method and may cause problems.
# If we're working with a bigger project that has a lot of same named functions, there's a risk of overwrite them instead of importing.
# It's actually better to use previous approaches. However this one is valid too.
