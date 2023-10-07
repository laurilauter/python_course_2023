"""TK1."""


def format_time(minutes: int) -> str:
    """
    Given minutes as an int, return correctly formatted time in hours and minutes.

    Correct format would be '{hours}h {minutes}min'.
    However, if there is not enough minutes to form an hour, show only minutes.
    In that case the format would be '{minutes}min'.
    But when there are no remaining minutes, show only hours.
    In that case the format would be '{hours}h'.
    One hour contains of 60 minutes.

    Examples:
    1) format_time(112) => '1h 52min'.
    2) format_time(23) => '23min'.
    3) format_time(180) => '3h'.

    :param minutes: given minutes
    :return: formatted time in hours and minutes
    """
    hours = minutes // 60
    minutes = minutes % 60
    if hours == 0:
        return f"{minutes}min"
    elif minutes == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {minutes}min"


def caught_speeding(speed: int, is_birthday: bool) -> int:
    """
    Return which category speeding ticket you would get.

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result, encoded as an int value:
    0=no ticket, 1=small ticket, 2=big ticket.
    If speed is 60 or less, the result is 0.
    If speed is between 61 and 80 inclusive, the result is 1.
    If speed is 81 or more, the result is 2.
    Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

    caught_speeding(60, False) => 0
    caught_speeding(65, False) => 1
    caught_speeding(65, True) => 0

    :param speed: Speed value.
    :param is_birthday: Whether it is your birthday (boolean).
    :return: Which category speeding ticket you would get (0, 1, 2).
    """
    if speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2


def first_half(text: str) -> str:
    """
    Return the first half of an string.

    The length of the string is even.

    first_half('HaaHoo') => 'Haa'
    first_half('HelloThere') => 'Hello'
    first_half('abcdef') => 'abc'
    """
    first_portion = len(text) // 2
    return text[:first_portion]


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    smaller_element = min(nums[0], nums[-1])

    if smaller_element < len(nums):
        return nums[smaller_element]
    else:
        return smaller_element


def remove_in_middle(text: str, to_remove: str) -> str:
    """
    Remove substring from the text, except for the first and the last occurrence.

    remove_in_middle("abc", "def") => "abc"
    remove_in_middle("abcabcabc", "abc") => "abcabc"
    remove_in_middle("abcdabceabcabc", "abc") => "abcdeabc"
    remove_in_middle("abcd", "abc") => "abcd"
    remove_in_middle("abcdabc", "abc") => "abcdabc"
    remove_in_middle("ABCAaaaAA", "a") => "ABCAaaAA

    :param text: string from where the remove takes place.
    :param to_remove: substring to be removed.
    :return: string with middle substrings removed.
    """
    first_index = text.find(to_remove)
    last_index = text.rfind(to_remove)

    if first_index == last_index:
        return text

    return text[:first_index] + text[last_index + len(to_remove):]


if __name__ == '__main__':

    print()
    print(format_time(112))  # = > '1h 52min'.
    print(format_time(23))  # = > '23min'.
    print(format_time(180))  # = > '3h'.

    print(caught_speeding(60, False))  # = > 0
    print(caught_speeding(65, False))  # = > 1
    print(caught_speeding(65, True))  # = > 0

    print(first_half('HaaHoo'))  # = > 'Haa'
    print(first_half('HelloThere'))  # = > 'Hello'
    print(first_half('abcdef'))  # = > 'abc'

    print(num_as_index([1, 2, 3]))  #
    print(num_as_index([4, 5, 6]))  #
    print(num_as_index([0, 1, 0]))  #
    print(num_as_index([3, 5, 6, 1, 1]))  #

    print(remove_in_middle("abc", "def"))  # = > "abc"
    print(remove_in_middle("abcabcabc", "abc"))  # = > "abcabc"
    print(remove_in_middle("abcdabceabcabc", "abc"))  # = > "abcdeabc"
    print(remove_in_middle("abcd", "abc"))  # = > "abcd"
    print(remove_in_middle("abcdabc", "abc"))  # = > "abcdabc"
    print(remove_in_middle("ABCAaaaAA", "a"))  # = > "ABCAaaAA
