"""Test cases for solution."""
from password import is_correct_length


def test__is_correct_length__too_short():
    """The one with the coffee at noon."""
    assert is_correct_length("1234567") is False


def test__is_correct_length__too_long():
    """The one with the coffee at noon."""
    assert is_correct_length("12345678901234567890123456"
                             "789012345678901234567890123456789012345") is False


def test__is_correct_length__min_value():
    """The one with the coffee at noon."""
    assert is_correct_length("12345678") is True


def test__is_correct_length__max_value():
    """The one with the coffee at noon."""
    assert is_correct_length("1234567890123456789012345678901"
                             "234567890123456789012345678901234") is True


def test__is_correct_length__empty():
    """The one with the coffee at noon."""
    assert is_correct_length("") is False


if __name__ == '__main__':

    test__is_correct_length__too_short()
    test__is_correct_length__too_long()
    test__is_correct_length__min_value()
    test__is_correct_length__max_value()
    test__is_correct_length__empty()
