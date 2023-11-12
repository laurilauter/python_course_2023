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
    assert includes_uppercase("nUotfi34534534534534rsT") is True


def test__includes_uppercase__only_uppercase_letters():
    """The one with the coffee at noon."""
    assert includes_uppercase("ABCDEFGI") is True


def test__includes_uppercase__every_uppercase_letter():
    """The one with the coffee at noon."""
    assert includes_uppercase("ABCDEFGHIJKLMNOPQRSTUVWXYZÜÕÖÄ") is True


def test__includes_lowercase__empty():
    """The one with the coffee at noon."""
    assert includes_lowercase("") is False


def test__includes_lowercase__includes_number():
    """The one with the coffee at noon."""
    assert includes_lowercase("1234567890") is False


def test__includes_lowercase__true_but_lowercase_not_first():
    """The one with the coffee at noon."""
    assert includes_lowercase("1234s5678a90") is True


def test__includes_lowercase__only_lowercase_letters():
    """The one with the coffee at noon."""
    assert includes_lowercase("abcsdfgsdgsgd") is True


def test__includes_lowercase__every_lowercase_letter():
    """The one with the coffee at noon."""
    assert includes_lowercase("abcdefghijklmnopqrstuvwxyzüõöä") is True


def test__includes_special__empty():
    """The one with the coffee at noon."""
    assert includes_special("") is False


def test__includes_special__includes_whitespace():
    """The one with the coffee at noon."""
    assert includes_special("ghjghj ghjghj") is True


def test__includes_special__no_special():
    """The one with the coffee at noon."""
    assert includes_special("abcsdAsgd") is False


def test__includes_special__several_different_special():
    """The one with the coffee at noon."""
    assert includes_special("abcs!dA@#$%^&*()<s>gd") is True


def test__includes_number__empty():
    """The one with the coffee at noon."""
    assert includes_number("") is False


def test__includes_number__every_digit():
    """The one with the coffee at noon."""
    assert includes_number("Aa0123456789") is True


def test__includes_number__no_digits():
    """The one with the coffee at noon."""
    assert includes_number("abcsdAsgd") is False


def test__includes_number__true_but_number_not_first():
    """The one with the coffee at noon."""
    assert includes_number("abcsdAsgd123") is True


def test__is_different__new_pass_case_sensitive():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("password", "PASSWORD") is False


def test__is_different__old_pass_case_sensitive():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("PASSWORD", "password") is False

# odd


def test__is_different__new_pass_odd_length__barely_different():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("1Password", "1Pasxxxxx") is True


def test__is_different__new_pass_odd_length__barely_different__reverse():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("1Pasxxxxx", "1Pasyyyyy") is True


def test__is_different__new_pass_odd_length__barely_not_different():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("1Password", "1Passxxxx") is False


def test__is_different__new_pass_odd_length__barely_not_different__not_in_beginning():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("zword1Passz", "zxxxx1Passz") is False


def test__is_different__new_pass_odd_length__barely_not_different__not_in_beginning_reverse():
    """The one with the coffee at noon."""
    assert is_different_from_old_password("zxxxx1Passz", "zword1Passz") is False

#  even


if __name__ == '__main__':

    test__is_correct_length__too_short()
    test__is_correct_length__too_long()
    test__is_correct_length__min_value()
    test__is_correct_length__max_value()
    test__is_correct_length__empty()

    test__includes_uppercase__empty()
    test__includes_uppercase__includes_number()
    test__includes_uppercase__true_but_uppercase_not_first()
    test__includes_uppercase__only_uppercase_letters()
    test__includes_uppercase__every_uppercase_letter()

    test__includes_lowercase__empty()
    test__includes_lowercase__includes_number()
    test__includes_lowercase__true_but_lowercase_not_first()
    test__includes_lowercase__only_lowercase_letters()
    test__includes_lowercase__every_lowercase_letter()

    test__includes_special__empty()
    test__includes_special__includes_whitespace()
    test__includes_special__no_special()
    test__includes_special__several_different_special()

    test__includes_number__empty()
    test__includes_number__every_digit()
    test__includes_number__no_digits()
    test__includes_number__true_but_number_not_first()

    test__is_different__new_pass_case_sensitive()
    test__is_different__old_pass_case_sensitive()

    test__is_different__new_pass_odd_length__barely_different()
    test__is_different__new_pass_odd_length__barely_different__reverse()
    test__is_different__new_pass_odd_length__barely_not_different()
    test__is_different__new_pass_odd_length__barely_not_different__not_in_beginning()
    test__is_different__new_pass_odd_length__barely_not_different__not_in_beginning_reverse()
