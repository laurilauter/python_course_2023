
"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """
    amount_of_uppercase = 0
    amount_of_lowercase = 0
    sum_of_numbers = 0
    for character in letter:
        if character.isupper():
            amount_of_uppercase += 1
        if character.islower():
            amount_of_lowercase += 1
        if character.isnumeric():
            sum_of_numbers += int(character)

    if amount_of_lowercase < amount_of_uppercase and amount_of_uppercase >= sum_of_numbers >= amount_of_lowercase:
        return True
    return False


if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True
