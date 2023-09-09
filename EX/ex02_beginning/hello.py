"""EX02 Hello."""


def main():
    """EX02 Hello."""

    """
    Print Hello
    Example output:
    
    What is your name? Mari
    Hello, Mari! Enter a random number: 5
    Great! Now enter a second random number: 4
    5 + 4 is 9
    
    """
    # ask for a name
    name = input("What is your name?")
    # ask for first random number
    print(f"Hello, {name}!", end=" ")
    num1 = int(input("Enter a random number:"))
    # ask for second random number
    print("Great!", end=" ")
    num2 = int(input("Now enter a second random number:"))
    # print out sum
    print(f"{num1} + {num2} is {str(num1 + num2)}")


if __name__ == '__main__':
    main()
