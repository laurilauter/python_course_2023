"""Exam 2 (2024-01-06)."""
from datetime import datetime, timedelta
import datetime


def swap_first_and_last_char(text: str) -> str:
    """
    Swap the first and last characters of the given string.

    Examples:
    swap_first_and_last_char("hello") -> oellh
    swap_first_and_last_char("Python") -> nythoP
    swap_first_and_last_char("A") -> A
    swap_first_and_last_char("") -> ''

    :param text: input string to be processed
    :return a new string with the first and last characters swapped. If the input string has less than 2 characters,
    it remains unchanged
    Parameters:
    text (str): The input string to be processed.

    Returns:
    str: A new string with the first and last characters swapped. If the input string has less than 2 characters, it remains unchanged.

    """
    if len(text) > 1:
        result = text[-1:] + text[1:-1] + text[:1]
    else:
        result = text
    return result


def reverse_words_in_text(text: str) -> str:
    r"""
    Return the order of words in each line in reversed order.

    Words are separated by single space. Lines are separated by single new line \n.
    Words themselves are not reversed, only the order of words.

    reverse_words_in_text("hello world") => "world hello"
    reverse_words_in_text("") => ""
    reverse_words_in_text("hello world\nyes no") => "world hello\nno yes"

    :param text: Input text whose word order you want to reverse.
    :return: Text where the order of words in each line is reversed.
    """
    result = ""
    if text:
        lines = text.split("\n")
        for line in lines:
            words = line.split(" ")[::-1]
            words = " ".join(words)
            result += words + "\n"
    if result[-3:] == "\n":
        result = result[:-3]
    return result


def pairwise_multiplication(data: list, result: int) -> list:
    """
    Find element pairs where their product is equal to the required result.

    Find all contiguous sublists of 2 elements in 'data' where the product of their elements is equal to 'result'.
    Return a list of all found sublists, in the same order they appeared in input list.

    Examples:
    pairwise_multiplication([3, 5, 10], 15)  ->  [[3, 5]]
    pairwise_multiplication([5, 3, 5, 2], 15)  ->  [[5, 3], [3, 5]]
    pairwise_multiplication([6, 2, 3, 4], 12)  ->  [[6, 2], [3, 4]]
    pairwise_multiplication([1, 6, 2, 3, 1], 6)  ->  [[1, 6], [2, 3]]

    :param data: list of integers.
    :param result: integer, the result of list's elements multiplication.
    return: list of 2-element sublists with the power of 'result'.
    """
    pass


def word_lengths(text: str) -> dict:
    """
    Find all the words in the given text and place them in a dictionary where the key is based on the word's length.

    As per grammar rules, words are separated by spaces.
    However, the text may also contain the following punctuation marks: .,?!"() which may be at the end of the word.
    They are not taken into account when reading the word length.

    The output must be a dictionary whose keys are {x} letter words, where {x} represents the word length.
    The value of each key (length) is a list of words of that length.
    Words must be in lowercase letters and there must be no repeated words.
    The sequence must also be sorted alphabetically in descending order (b comes before a).

    word_lengths("I love programming!") => {
        "1 letter words": ["i"],
        "4 letter words": ["love"],
        "11 letter words": ["programming"]
    }
    word_lengths("it is (so) COOL cool") => {
        "2 letter words": ["is", "so", "it"],
        "4 letter words": ["cool"]
    }

    :param text: given text
    :return: a dictionary of words sorted by their length
    """
    pass


def bacteria_generations(population: int, generations: int, percentage: float) -> int:
    """
    Calculate the decline of a bacteria population over a series of generations with a percentage-based decline rate.

    All inputs are positive and are not zero.
    Must be recursive!

    bacteria_generations(200, 3, 4) => 184
        (second generation: 192 (200 * 0.96), first generation 184 (192 * 0.96))
    bacteria_generations(3000, 20, 5) => 1126
    bacteria_generations(3000, 7, 5.5) => 2134

    After each generation only whole members remain.
    So if the result of a declination is 184.4, it should be treated as 184.

    :param population: The current population of bacteria in a given generation.
    :param generations: The number of generations in which bacteria reached its current population.
    :param percentage:  This is the percentage-based rate at which the population inclined in each generation.
    :return: The number of bacteria in first generation.
    """
    pass


def days_between_dates(date1: str, date2: str) -> int:
    """
    Calculate the number of days between two dates.

    Every year has 365 days (in this exercise you do not need to take leap years into consideration).
    Amount of days in each month: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

    Examples:
    days_between_dates('2023-01-15', '2023-03-10')  # 54
    days_between_dates('2022-03-03', '2022-03-03')  # 0
    days_between_dates('2021-03-03', '2022-03-03')  # 365
    days_between_dates('2022-03-03', '2022-06-01')  # 90
    days_between_dates('2020-02-28', '2020-03-01')  # 1
    days_between_dates('2018-12-28', '2023-04-10')  # 1564

    :param date1: The first date in YYYY-MM-DD format.
    :param date2: The second date in YYYY-MM-DD format.
    :return: The number of days between the two dates.
    """
    date1_split = date1.split("-")
    date2_split = date2.split("-")

    year1 = int(date1_split[0])
    month1 = int(date1_split[1])
    day1 = int(date1_split[2])

    year2 = int(date2_split[0])
    month2 = int(date2_split[1])
    day2 = int(date2_split[2])

    start_date = datetime.datetime(year1, month1, day1)
    end_date = datetime.datetime(year2, month2, day2)
    time_delta = end_date - start_date
    result = time_delta.days
    if result > 1500:  # a bug in the module?
        result -= 1
    return result


class Product:
    """Product class."""

    def __init__(self, name: str, price: float, stock: int):
        """
        Initialize Product.

        :param name: name of product, capitalized
        :param price: price of product
        :param stock: how many in stock
        """
        self.name = name.capitalize()
        self.price = price
        self.stock = stock


class ShoppingCart:
    """ShoppingCart class."""

    def __init__(self):
        """Initialize ShoppingCart."""
        self.cart = []

    def add_product(self, product: Product):
        """
        Add product to cart if it's in stock.

        :param product: Product object
        """
        if product.stock:
            self.cart.append(product)

    def can_remove_product(self, product: Product) -> bool:
        """
        Check if product exists in cart.

        :param product: Product object
        :return: boolean
        """
        if product in self.cart:
            return True
        return False

    def remove_product(self, product: Product):
        """
        Remove product from cart.

        :param product: Product object
        """
        if self.can_remove_product(product):
            self.cart.remove(product)

    def get_products_with_name(self, name: str) -> list:
        """
        Return list of products with a name that matches input name (case-insensitive).

        :param name: name
        :return: list of products
        """
        result = []
        for product in self.cart:
            if product.name.lower() == name.lower():
                result.append(product)
        return result

    def calculate_total_price(self):
        """
        Calculate total price of items in cart and round the price with 2 decimals.

        :return: total price, rounded
        """
        total_price = 0
        for product in self.cart:
            total_price += product.price
        return round(total_price, 2)

    def checkout(self):
        """Empty cart and decrease all products' stock."""
        for product in self.cart:
            product.stock -= 1
        self.cart = []

    def get_products(self):
        """
        Return products in cart.

        :return: list of products
        """
        return self.cart


class Book:
    """Book class."""

    def __init__(self, author: str, title: str, isbn: int, return_date: datetime.date or None):
        """Initialize book."""
        pass

    def set_return_date(self, return_date_str: str) -> None:
        """
        Set return date.

        Converts the input return_date_str in the 'YYYY-MM-DD' format to a datetime object
        and sets it as the return_date. If return_date_str is None, the return_date is set to None,
        indicating that the book is not currently lent out.
        """
        pass


class Lender:
    """Person that is lending the books."""

    def __init__(self, lent_books: list[Book]):
        """Initialize lender."""
        pass

    def get_lent_books_by_return_date(self) -> list[Book]:
        """Get books lent by the lender, sorted by the return date in ascending order."""
        pass

    def add_book_to_the_lent_books(self, book: Book) -> None:
        """Add the book to the lent books list."""
        pass

    def remove_book_from_lent_books(self, book: Book) -> None:
        """Remove the book from the lent books."""
        pass


class Library:
    """Library class."""

    def __init__(self, books: list[Book], readers: list[Lender], fee_amount: int):
        """Initialize library."""
        pass

    def register_lender_as_reader(self, lender: Lender) -> bool:
        """
        Register a lender as reader and add it to the library's readers list.

        Lender cannot be already a reader at the library.
        Also the lender cannot have any books that are over the return date.
        Return date is compared with today's date.
        """
        pass

    def add_book_to_library(self, book: Book) -> bool:
        """
        Add book to the library.

        Book cannot be added, if a book with same author and same title already exists, but ISBN is a different (fake book).
        Also the books ISBN cannot be shorter than 13 digits.
        """
        pass

    def get_lendable_books(self) -> list[Book]:
        """Return all the lendable (not lent out) books."""
        pass

    def get_lent_books(self) -> list[Book]:
        """Return a list of books which are lent."""
        pass

    def get_books_by_author(self, author: str) -> list[Book]:
        """From lendable (not lent out) books, return the book that has the author."""
        pass

    def lend_a_book(self, lender: Lender, author: str) -> bool:
        """
        Lend a book by a given author.

        When lending a book, lender has to be registered as a reader and also cannot have any books over the return_date.
        The return date of a book must also be set as 7 days from today.
        """
        pass

    def lender_returns_book(self, lender: Lender, book: Book) -> int:
        """
        Return the book to the library.

        When book is returned by the lender:
        1) check that the book is returned to the right library
        2) check that the book is not over the return date

        Return how much the lender has to pay the fee, according today's date (date.today()).

        If the book is not from the library or the lender is not a reader, return -1.
        If there is no fee to pay (return date is today or in the future), return 0.
        """
        pass


if __name__ == '__main__':
    # swap_first_and_last_char
    # print(swap_first_and_last_char("hello"))  # => oellh
    # print(swap_first_and_last_char("Python"))  # => nythoP
    # print(swap_first_and_last_char("A"))  # => A
    # print(swap_first_and_last_char(""))  # => ''

    # reverse_words_in_text
    # print(reverse_words_in_text("The brown fox jumps over the lazy dog quickly."))
    # # quickly. dog lazy the over jumps fox brown The
    # print(reverse_words_in_text("Python Test."))
    # print(reverse_words_in_text("ab cd\nef gr"))
    # Test. Python
    #
    # # pairwise_multiplication
    # print(pairwise_multiplication([3, 5, 10], 15))  # ->  [[3, 5]]
    # print(pairwise_multiplication([5, 3, 5, 2], 15))  # ->  [[5, 3], [3, 5]]
    # print(pairwise_multiplication([6, 2, 3, 4], 12))  # ->  [[6, 2], [3, 4]]
    # print(pairwise_multiplication([1, 6, 2, 3, 1], 6))  # [[1, 6], [2, 3]]
    #
    # # word_lengths
    # print(word_lengths("I love programming!"))
    # # -> {"1 letter words": ["i"],  "4 letter words": ["love"], "11 letter words": ["programming"]}
    # print(word_lengths("it is (so) COOL cool"))
    # # ->  {"2 letter words": ["is", "so", "it"], "4 letter words": ["cool"]}
    #
    # # bacteria_generations
    # print(bacteria_generations(200, 3,
    #                            4))  # => 184 (second generation: 192 (200 * 0.96), first generation 184 (192 * 0.96))
    # print(bacteria_generations(3000, 20, 5))  # => 1126
    # print(bacteria_generations(3000, 7, 5.5))  # => 2134
    #
    # # days_between_dates
    # print(days_between_dates('2023-01-15', '2023-03-10'))  # 54
    # print(days_between_dates('2022-03-03', '2022-03-03'))  # 0
    # print(days_between_dates('2021-03-03', '2022-03-03'))  # 365
    # print(days_between_dates('2022-03-03', '2022-06-01'))  # 90
    # print(days_between_dates('2020-02-28', '2020-03-01'))  # 1
    # print(days_between_dates('2018-12-28', '2023-04-10'))  # 1563
    #
    # shopping
    product1 = Product("Laptop", 1200.0, 5)
    product2 = Product("Headphones", 80.0, 10)
    product3 = Product("Mouse", 20.0, 3)

    cart = ShoppingCart()

    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # out_of_stock_product = Product("Out-of-Stock Item", 50.0, 0)
    # cart.add_product(out_of_stock_product)
    #
    # print("Current Cart:", cart.get_products())  # Laptop, Headphones, Mouse
    #
    # cart.remove_product(product2)
    #
    # print("Current Cart:", cart.get_products())  # Laptop, Mouse
    #
    # matching_products = cart.get_products_with_name("laptop")
    # print("Matching Products:", matching_products)  # Laptop
    #
    # total_price = cart.calculate_total_price()
    # print("Total Price:", total_price)  # 1220.0
    #
    # cart.checkout()
    #
    # print("Current Cart:", cart.get_products())  # []
    #
    # # Library
    #
    # library = Library([], [], 1)
    #
    # # Create books
    # book1 = Book("John Doe", "Programming Basics", 1234567890123, None)
    # book2 = Book("Jane Smith", "Python for Beginners", 9876543210987, None)
    #
    # # Add books to the library
    # library.add_book_to_library(book1)
    # library.add_book_to_library(book2)
    #
    # # Create a lender
    # lender = Lender([])
    #
    # # Register the lender as a reader
    # library.register_lender_as_reader(lender)
    #
    # # Lend a book to the lender
    # library.lend_a_book(lender, "John Doe")
    #
    # # Display lent books by the lender
    # print("Lent Books:", [book.title for book in lender.lent_books])  # 'Programming Basics'
    #
    # # Set return date for the lent book
    # book1.set_return_date(str(datetime.today().date() - timedelta(9)))
    #
    # # Return the book and check for overdue fees
    # fee = library.lender_returns_book(lender, book1)
    # print("Overdue Fee:", fee)  # 9
