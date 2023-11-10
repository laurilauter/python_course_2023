"""Test cases for solution."""
from EX.ex10_solution_and_tests.solution import students_study


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    assert students_study(12, True) is True
