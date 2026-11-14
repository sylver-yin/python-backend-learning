import random


class Die:
    """A simple class representing a single die."""

    def __init__(self, sides=6):
        """Initialise a classic D6 die."""
        self.sides = sides

    def describe_a_die(self):
        """Print a statement that describes which die is being rolled"""
        print(f"Now rolling a {self.sides}-sided die:")

    def roll_ten_times(self):
        """Rolls a random number between 1 and other side numbers for ten times."""
        self.roll_times = 0
        while True:
            if self.roll_times >= 10:
                break
            else:
                random_number = random.randint(1, self.sides)
                print(random_number)
                self.roll_times += 1


six_sided_die = Die()
six_sided_die.describe_a_die()
six_sided_die.roll_ten_times()
ten_sided_die = Die(10)
ten_sided_die.describe_a_die()
ten_sided_die.roll_ten_times()
twenty_sided_die = Die(20)
twenty_sided_die.describe_a_die()
twenty_sided_die.roll_ten_times()
