"""Entry."""
import re


def parse(row: str) -> tuple:
    """
    Parse string row into a tuple.

    The row has a first name, last name, ID code, phone number, date of birth and address.
    Only ID code is mandatory, other values may not be included.

    They can be found by the following rules:
    - Both the first name and last name begin with a capital letter and are followed by a lowercase letter
    - ID code is an 11-digit number
    - Phone number has the same rules applied as in the previous task
    - Date of birth is in the form of dd-MM-YYYY
    - Address is everything else that's left

    :param row: given string to find values from
    :return: tuple of values found in given string
    """
    #regex = r'([A-ZÜÕÖÄ][a-züõöä]+)?([A-ZÜÕÖÄ][a-züõöä]+)?(\d{11})(\+\d{3}[- ]?\d{7,8})?(\d{2}-\d{2}-\d{4})?(.*)?'
    regex = r'([A-ZÜÕÖÄ][a-züõöä]+)?([A-ZÜÕÖÄ][a-züõöä]+)?(\d{11})((\+\d{3}[- ])?\d{7,8})?(\d{2}-\d{2}-\d{4})?(.*)?'
    matches = re.findall(regex, row)
    new_text = re.sub(r"''", 'None', ''.join(map(str, matches)))
    new_tuple = tuple(eval(new_text))
    return new_tuple


if __name__ == '__main__':
    # print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # # ('Priit', 'Pann', '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    #
    # print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # # (None, None, '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    #
    # print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    # # ('Priit', 'Pann', '39712047623', None, '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    # #
    # print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    # # ('Priit', 'Pann', '39712047623', '+372 56887364', None, 'Oja 18-2,Pärnumaa,Are')

    print(parse('39712047623'))
    # (None, None, '39712047623', None, None, None)
