"""EX02 ATM."""


def main():
    """
    Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

    Given the sum, one must print out how many banknotes does it take to cover the sum. Task is to cover the sum with as little
    banknotes as possible.

    Example
    The sum is 72€
    We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
    """

    amount = int(input("Enter a sum: "))
    banknote_types = [100, 50, 20, 10, 5, 1]
    banknotes = 0

    while amount > 0:
        for banknote_type in banknote_types:
            notes_to_add = amount // banknote_type
            banknotes += notes_to_add
            amount -= notes_to_add * banknote_type

    print(f"Amount of banknotes needed: {banknotes}")


if __name__ == '__main__':
    main()
