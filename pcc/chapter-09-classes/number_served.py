class Restaurant:
    """Simple modeling of restaurant's info."""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 50

    def describe_restaurant(self):
        print(
            f'\nThe restaurant is called "{self.name}". The cuisine is {self.cuisine}. Customers served: {self.number_served}'
        )

    def open_restaurant(self):
        print(f"The {self.name} is currently open.")

    def set_number_served(self, new_customers_quantity):
        if new_customers_quantity >= self.number_served:
            self.number_served = new_customers_quantity
        else:
            print("Added customers can't be a negative value.")

    def increment_number_served(self, new_customers):
        if new_customers >= 0:
            self.number_served += new_customers
        else:
            print("You can't add a negative number.")


restaurant = Restaurant("Fork and Pie", "British")
restaurant.describe_restaurant()

restaurant.set_number_served(80)
restaurant.describe_restaurant()

restaurant.increment_number_served(1)
restaurant.describe_restaurant()
