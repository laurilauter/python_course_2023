"""Test cases for solution."""
from solution import students_study
from solution import lottery
from solution import fruit_order


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


#  LOTTERY TESTS
def test_lottery_all_cases():
    """The lottery."""
    assert lottery(5, 5, 5) == 10
    assert lottery(-5, -5, -5) == 5
    assert lottery(0, 0, 0) == 5
    assert lottery(4, 4, 4) == 5
    assert lottery(2, 2, 1) == 0
    assert lottery(2, 3, 1) == 1
    assert lottery(2, 3, 2) == 0
    assert lottery(2, 3, 3) == 1


def test_fruit_order_all_zero():
    """Fruit order."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order_zero_amount_zero_small():
    """Fruit order."""
    assert fruit_order(0, 6, 0) == -1


def test_fruit_order_zero_amount_zero_big():
    """Fruit order."""
    assert fruit_order(6, 0, 0) == 0


# def test_fruit_order_zero_amount_others_not_zero():
#     """Fruit order."""
#     assert fruit_order(6, 6, 0) == -1
#
#
def test_fruit_order_zero_only_big_exact_match():
    """Fruit order."""
    assert fruit_order(0, 2, 10) == 0


def test_fruit_order_only_big_not_enough_but_multiple_of_5():
    """Fruit order."""
    assert fruit_order(0, 2, 15) == -1


def test_fruit_order_only_small_exact_match():
    """Fruit order."""
    assert fruit_order(3, 0, 3) == 3


def test_fruit_order_only_small_not_enough():
    """Fruit order."""
    assert fruit_order(3, 0, 4) == -1


def test_fruit_order_only_small_more_than_required():
    """Fruit order."""
    assert fruit_order(5, 0, 4) == 4


def test_fruit_order_match_with_more_than_5_smalls():
    """Fruit order."""
    assert fruit_order(6, 0, 6) == 6


def test_fruit_order_all_positive_exact_match():
    """Fruit order."""
    assert fruit_order(6, 1, 11) == 6


def test_fruit_order_use_all_smalls_some_bigs():
    """Fruit order."""
    assert fruit_order(6, 3, 16) == 1


def test_fruit_order_use_some_smalls_all_bigs():
    """Fruit order."""
    assert fruit_order(6, 3, 17) == 2


def test_fruit_order_use_some_smalls_some_bigs():
    """Fruit order."""
    assert fruit_order(6, 2, 8) == 3


def test_fruit_order_not_enough():
    """Fruit order."""
    assert fruit_order(6, 1, 20) == -1


def test_fruit_enough_bigs_not_enough_smalls():
    """Fruit order."""
    assert fruit_order(3, 1, 14) == -1


def test_fruit_not_enough_with_more_than_5_smalls():
    """Fruit order."""
    assert fruit_order(1, 4, 22) == -1


def test_fruit_enough_bigs_not_enough_smalls_large_numbers():
    """Fruit order."""
    assert fruit_order(21, 100, 522) == -1


def test_fruit_match_large_numbers():
    """Fruit order."""
    assert fruit_order(66, 100, 566) == 66


if __name__ == '__main__':

    test_students_study_during_day()
    test_students_study_during_evening()
    test_students_study_during_night()
    test_students_study_random()
    test_lottery_all_cases()

    test_fruit_order_all_zero()
    test_fruit_order_zero_amount_zero_small()
    test_fruit_order_zero_amount_zero_big()
    # test_fruit_order_zero_amount_others_not_zero()
    test_fruit_order_zero_only_big_exact_match()

    test_fruit_order_only_big_not_enough_but_multiple_of_5()

    test_fruit_order_only_small_exact_match()
    test_fruit_order_only_small_not_enough()
    test_fruit_order_only_small_more_than_required()
    test_fruit_order_match_with_more_than_5_smalls()
    test_fruit_order_all_positive_exact_match()
    test_fruit_order_use_all_smalls_some_bigs()
    test_fruit_order_use_some_smalls_all_bigs()
    test_fruit_order_use_some_smalls_some_bigs()
    test_fruit_order_not_enough()
    test_fruit_enough_bigs_not_enough_smalls()
    test_fruit_not_enough_with_more_than_5_smalls()
    test_fruit_enough_bigs_not_enough_smalls_large_numbers()
    test_fruit_match_large_numbers()
