import pytest  # type: ignore
from employee import Employee


@pytest.fixture
def employee_instance():
    custom_employee = Employee("john", "pork", 73000)
    return custom_employee


def test_give_default_salary(employee_instance):
    """Test if standard class behavior is working properly."""
    employee_instance.give_raise()
    assert employee_instance.annual_salary == 78000


def test_give_custom_salary(employee_instance):
    """Testing if custom behavior works as well"""
    employee_instance.give_raise(7000)
    assert employee_instance.annual_salary == 80000
