"""Test cases for solution."""
from EX.ex10_solution_and_tests.solution import students_study


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    assert students_study(18, True) is True
    assert students_study(24, True) is True
    assert students_study(18, False) is True
    assert students_study(24, False) is True

    assert students_study(1, True) is False
    assert students_study(4, True) is False
    assert students_study(1, False) is False
    assert students_study(4, False) is False

    assert students_study(5, True) is True
    assert students_study(17, True) is True
    assert students_study(5, False) is False
    assert students_study(17, False) is False
    assert students_study(12, True) is True
