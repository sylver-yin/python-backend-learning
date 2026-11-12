import pytest
from employee import Employee


def test_give_default_salary():
    """Test if standard class behavior is working properly."""
    employee_instance = Employee("john", "pork", 73000)
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 78000


def test_give_custom_salary():
    """Testing if custom behavior works as well"""
    employee_instance = Employee("john", "pork", 73000)
    employee_instance.give_raise(7000)
    assert employee_instance.annual_salary == 80000
