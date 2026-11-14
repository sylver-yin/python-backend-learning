class Employee:
    """A simple class that imitates an employee."""

    def __init__(self, first, last, annual_salary):
        """Store the first name, last name and the annual salary of the employee."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, added_money=5000):
        """Raise the employee and their salary by $5000 by default but accepts other values"""
        self.annual_salary += added_money
        return self.annual_salary
