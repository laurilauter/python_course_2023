"""Control number."""


def control_number(encrypted_string: str) -> bool:
    """
    Given encrypted string that has a control number in the end of it, return True if correct, else False.

    Calculating the correct control number:
    1. Start the calculation from 0.
    2. Add 1 for every lowercase occurrence.
    3. Add 2 for every uppercase occurrence.
    4. Add 5 for any of the following symbol occurrences: "?!@#".
    Other symbols/letters/digits don't affect the result.

    NB! If for example the number you come up with is 25, you only have to check the last two digits of the string.
    e.g. control_number("?!?!#4525") -> True, because it ends with 25.

    :param encrypted_string: encrypted string
    :return: validation
    """

    def calculate_number(string):
        calculated_number = 0
        for character in string:
            if character.islower():
                calculated_number += 1
            if character.isupper():
                calculated_number += 2
            if character in "?!#@":
                calculated_number += 5
        return calculated_number

    def check_calculated_number(number, string):
        end_of_string = string[-(len(str(number))):]

        if end_of_string.isnumeric():
            number_in_string = int(end_of_string)
            if number == number_in_string:
                return True
        return False

    calculated_control_number = calculate_number(encrypted_string)
    return check_calculated_number(calculated_control_number, encrypted_string)


if __name__ == '__main__':
    print(control_number("mE0W5"))  # True
    print(control_number("SomeControlNR?20"))  # False
    print(control_number("False?Nr9"))  # False
    print(control_number("#Hello?!?26"))  # True
    print(control_number("3423982340000000.....///....0"))  # True
    print(control_number("#Shift6"))  # False
