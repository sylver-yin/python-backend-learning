class Restaurant:
    """A simple modeling of restaurant."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Print a statement that describes restaurant neatly organised."""
        print(
            f'Restaurant is called "{self.name.title()}". The cuisine is {self.cuisine}. It served {self.number_served} customers'
        )

    def open_restaurant(self):
        """Print a statement that states that restaurant is open."""
        print(f'"{self.name.title()}" is now open!')

    def set_number_served(self, served_clients):
        """Set the number of served client. Rejects lesser or negative number."""
        if served_clients >= self.number_served:
            self.number_served = served_clients
        else:
            print("Please, state a valid number.")

    def increment_customer_served(self, added_clients):
        """Increment the number of served customer. Rejects invalid number."""
        if added_clients >= 0:
            self.number_served += added_clients
        else:
            print("Please, state a valid number.")


class IceCreamStand(Restaurant):
    """A simple attempt to write a ice cream stand restaurant type."""

    def __init__(self, name, cuisine):
        """Initialise given data. Then adds the attributes that represent an ice cream stand."""
        super().__init__(name, cuisine)
        self.flavors = ["blueberry", "mango", "bubblegum"]

    def describe_restaurant(self):
        """Print a statement that describes restaurant neatly organised."""
        print(
            f'This stand serves {self.cuisine}. The ice cream stand is called "{self.name.title()}". It served {self.number_served} customers'
        )

    def display_flavors_list(self):
        """Display the list of ice cream flavors."""
        print("These are the flavors we have:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_shop = IceCreamStand("Joe's", "ice cream")
ice_cream_shop.set_number_served(95)
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors_list()
