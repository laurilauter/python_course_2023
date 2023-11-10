"""Test cases for solution."""
from solution import *


def test_students_study_during_day():
    """
    The one with the coffee at noon.

    During the day, students study when there is coffee.
    This case represents the time period of a day and coffee is present.
    Expected result: True.
    """
    assert students_study(5, True) is True
    assert students_study(17, True) is True
    assert students_study(5, False) is False
    assert students_study(17, False) is False
    assert students_study(12, True) is True


def test_students_study_during_evening():
    """The one with the coffee at evening."""

    assert students_study(18, True) is True
    assert students_study(24, True) is True
    assert students_study(18, False) is True
    assert students_study(24, False) is True


def test_students_study_during_night():
    """The one with the coffee at night."""
    assert students_study(1, True) is False
    assert students_study(2, True) is False
    assert students_study(3, True) is False
    assert students_study(4, True) is False
    assert students_study(1, False) is False
    assert students_study(2, False) is False
    assert students_study(3, False) is False
    assert students_study(4, False) is False


def test_students_study_random():
    """The one with the coffee at random."""
    assert students_study(0, True) is False
    assert students_study(-4, True) is False
    assert students_study(25, False) is False


if __name__ == '__main__':

    test_students_study_during_day()
    test_students_study_during_evening()
    test_students_study_during_night()
    test_students_study_random()
