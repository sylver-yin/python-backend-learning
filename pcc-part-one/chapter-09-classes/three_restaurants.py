class Restaurant:  # NOTE: I could've just import but I didn't want the 9-1 calls in the terminal.
    """Simple modeling of restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f'\nRestaurant is called "{self.name}"; the cuisine is {self.cuisine}')


restaurant_chinese = Restaurant("李米的小面食堂", "chinese")
restaurant_british = Restaurant("The Fork and the Pie", "british")
restaurant_ukrainian = Restaurant("Італієць", "ukrainian")

restaurant_chinese.describe_restaurant()

restaurant_british.describe_restaurant()

restaurant_ukrainian.describe_restaurant()
