"""Test cases for solution."""
from password import is_correct_length


def test__is_correct_length__too_short():
    """The one with the coffee at noon."""
    assert is_correct_length("1234567") is False


def test__is_correct_length__too_long():
    """The one with the coffee at noon."""
    assert is_correct_length("1234567890123456789012345678901234567890123456789012345678901234567890") is False


if __name__ == '__main__':

    test__is_correct_length__too_short()