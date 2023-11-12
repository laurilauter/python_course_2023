"""Test cases for solution."""
from password import is_correct_length
from password import includes_uppercase
from password import includes_lowercase
from password import includes_special
from password import includes_number
from password import is_different_from_old_password
from password import is_name_in_password
from password import is_birthday_in_password
from password import is_password_valid


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


def test__includes_uppercase__empty():
    """The one with the coffee at noon."""
    assert includes_uppercase("") is False


def test__includes_uppercase__includes_number():
    """The one with the coffee at noon."""
    assert includes_uppercase("1234567890") is False


def test__includes_uppercase__true_but_uppercase_not_first():
    """The one with the coffee at noon."""
    assert includes_uppercase("notfirsT") is True


if __name__ == '__main__':

    test__is_correct_length__too_short()
    test__is_correct_length__too_long()
    test__is_correct_length__min_value()
    test__is_correct_length__max_value()
    test__is_correct_length__empty()

    test__includes_uppercase__empty()
    test__includes_uppercase__includes_number()
    test__includes_uppercase__true_but_uppercase_not_first()
