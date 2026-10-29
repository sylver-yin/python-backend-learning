class Restaurant:
    """Simple modeling of restaurant's info."""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f'The restaurant is called "{self.name}". The cuisine is {self.cuisine}')

    def open_restaurant(self):
        print(f"The {self.name} is currently open.")


restaurant = Restaurant("Kangaroo's dinner", "australian")

restaurant.describe_restaurant()
restaurant.open_restaurant()
