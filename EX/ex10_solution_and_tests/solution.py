"""Solution to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 1 <= time <= 4:
        return False
    if 18 <= time <= 24:
        return True
    if 5 <= time <= 17 and coffee_needed:
        return True
    return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if b != a and c != a:
        return 1
    if a == b == c and a != 5 and b != 5 and c != 5:
        return 5
    if a == 5 and b == 5 and c == 5:
        return 10
    return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    if ordered_amount - big_baskets * 5 - small_baskets == 0:
        return small_baskets
    return -1


if __name__ == '__main__':

    print(students_study(0, True))
    # print(students_study(1, True))
    # print(students_study(3, True))
    # print(students_study(4, True))
    # print(students_study(17, True))
    # print(students_study(18, True))
    # print(students_study(19, True))

    # print(lottery(5, 5, 5))  # 10
    # print(lottery(4, 4, 4))  # 5
    # print(lottery(2, 2, 1))  # 0
    # print(lottery(2, 3, 1))  # 1

    print(fruit_order(4, 1, 9))
    print(fruit_order(9, 0, 9))
    print(fruit_order(3, 1, 10))
