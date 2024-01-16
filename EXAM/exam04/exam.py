"""Exam 4 (2024-01-11)."""
from __future__ import annotations


def modify_string(text: str) -> str:
    """
    Modify a given string based on the following rules.

    - If the length of the string is less than 3, leave it unchanged.
    - If the string ends with 'ing', add 'ly'.
    - If none of the above conditions apply, add 'ing' at the end of the string.

    Parameters:
    text (str): The input string to be modified.

    Returns:
    str: The modified string based on the rules specified above.

    Example:
    modify_string("walk") => 'walking'
    modify_string("swimming") => 'swimmingly'
    modify_string("go") => 'go'
    modify_string("skiing") => 'skiingly'
    """
    # print(text[3:-1])
    if len(text) < 3:
        return text
    elif text[-3:].lower() == "ing":
        text += "ly"
        return text
    else:
        text += "ing"
        return text


def capitalize_first_last_letters(text: str) -> str:
    """
    Take a string and capitalize the first and last letter of each word while keeping the rest of the letters in lowercase.

    capitalize_first_last_letters("hello") => "HellO"
    capitalize_first_last_letters("hello world") => "HellO WorlD"
    capitalize_first_last_letters("") => ""
    capitalize_first_last_letters("hello! 2024") => "Hello! 2024"

    :param text: Input string in which you want to capitalize the first and last letters of each word. If there is a symbol after the letter, the letter is not capitalized.
    :return: Text where the size of the first and last letter of each word is changed.
    """
    test_list = text.split(" ")
    second_list = []
    for word in test_list:

        first = word[0].capitalize()
        last = word[-1].capitalize()
        word = first + word[1:-1] + last
        second_list.append(word)

    return " ".join(second_list)



def uno_game(hand: list, table: str) -> str:
    """
    Determine the outcome of a player's move in an UNO game based on the cards in hand and the card on the table.

    There are always at least 1 card in hand and exactly 1 card on the table.

    UNO Rules:
    A player can make a move if at least one of the following conditions is met:
    - There's a card in hand with the same color as the card on the table.
    - There's a card in hand with the same number as the card on the table.

     Return:
    - "Uno!" if after the move, there's only one card left in hand.
    - "Win!" if after the move, there are no cards left in hand.
    - "Continue..." in all other cases.

    uno_game(["yellow 3", "red 3"], "red 10") => "Uno!"
    uno_game(["blue 1"], "blue 5") => "Win!"
    uno_game(["blue 1", "green 2", "yellow 4", "red 2"], "blue 5") => "Continue..."
    """
    pass


def find_anagrams(words: list[str]) -> dict:
    """
    Find anagrams in the list of words.

    The function returns a dictionary where each key is a word from the input list, and the value is a list
    of words from the input list that are anagrams of the key. Don't add the original word to the return list.
    The comparison is case-insensitive (A == a). In the result, all the strings are in lower case.
    If there are no anagrams (which are different from the original string), do not add the given word (the second example).
    If one word has multiple anagrams of the same value, only one is added (the last example).


    find_anagrams(["listen", "silent", "hello", "person", "nosrep", "world", "nistel"]) =>
    {
        'listen': ['silent', 'nistel'],
        'silent': ['listen', 'nistel'],
        'nistel': ['listen', 'silent'],
        'person': ['nosrep'],
        'nosrep': ['person']
    }

    find_anagrams(["hello", "hello"]) => {}
    find_anagrams(["hello", "hello", "Ohell"]) => {
        'hello': ['ohell'],
        'ohell': ['hello']
    }


    :param words: list of words
    :return: dictionary with anagrams
    """
    pass


def count_layers(pyramid: str) -> int:
    r"""
    Count the pyramid layers.

    Must be recursive!

    count_layers("") => 1

    count_layers(('*\n'
                 '***\n'
                '*****\n'
               '*******\n'
              '*********\n')) => 6

    count_layers(('n/*\n'
                 '/n***\n'
                '/n*****\n'
               '/n*******\n'
              '/n*********\n'
             '/n***********\n'
            '/n*************\n')) => 8

    count_layers(('aaa\n'
                  'aaa\n'
                  'aaa\n'
                  'aaa\n'
                  'aaa\n')) => 6
    count_layers(('  |  \n'
                  ' +-+ \n'
                  '<   >\n'
                  ' +-+ \n')) => 5

    :param pyramid: The pyramid that layers must be counted.
    :return: Amount of pyramid layers.
    """
    pass


def rhombus_pattern(n: int, with_spaces: bool) -> list[str]:
    """
    Generate a rhombus pattern.

    Given a positive integer n, generate a rhombus pattern, with 2n - 1  rows in rhombus.
    First row has 1 star, second 3, third 5... etc.
    After the n-th row star amount starts to decrease.
    If parameter with_spaces is True, instead of every second star in a row has to be space.

    Example:
    rhombus_pattern(4, False) =>
    [
        '   *   ',
        '  ***  ',
        ' ***** ',
        '*******',
        ' ***** ',
        '  ***  ',
        '   *   '
    ]
    rhombus_pattern(4, True) =>
    [
        '   *   ',
        '  * *  ',
        ' * * * ',
        '* * * *',
        ' * * * ',
        '  * *  ',
        '   *   '
    ]
    rhombus_pattern(2, False) =>
    [
        ' * ',
        '***',
        ' * '
    ]
    rhombus_pattern(0, False) =>
    []
    :param n: number of rows from start to the middle.
    :param with_spaces: rhombus pattern will be with spaces or not.
    :return: list with strings, that creates a rhombus pattern.
    """
    pass


class Song:
    """Song class."""

    def __init__(self, title: str, artist: str, duration: int):
        """
        Initialize Song.

        :param title: title of Song
        :param artist: Song artist
        :param duration: duration of Song (in seconds)
        """
        pass

    def __repr__(self) -> str:
        """Represent Song."""
        pass


class Playlist:
    """Playlist class."""

    def __init__(self):
        """Initialize Playlist."""
        pass

    def add_song(self, song: Song):
        """
        Add song to playlist if there is not a song in the Playlist with the same title and artist already.

        :param song: Song object to add
        """
        pass

    def remove_song(self, song: Song):
        """
        Remove song if it exists in Playlist.

        :param song: Song object to remove.
        """
        pass

    def get_duration_of_playlist(self) -> int:
        """
        Get the total duration of Playlist.

        :return: duration of Playlist
        """
        pass

    def get_songs_by_artist(self, artist: str) -> list[Song]:
        """
        Get all songs by given artist.

        The search is case-insensitive.

        :param artist: artist
        :return: songs by artist
        """
        pass

    def sort_songs_alphabetically(self) -> list[Song]:
        """
        Sort the Playlist songs alphabetically by title.

        :return: sorted Playlist
        """
        pass

    def get_longest_song(self) -> Song:
        """
        Get song from Playlist that has the longest duration.

        :return: longest Song
        """
        pass

    def get_songs(self) -> list[Song]:
        """Return all songs."""
        pass


class Dog:
    """Dog class."""

    def __init__(self, name: str, skills: list[str], toys: list[str]):
        """
        Initialize dog object.

        :param name: Name
        :param skills: list of skills (strings)
        :param toys: list of toy names (strings)
        """
        pass

    def __repr__(self) -> str:
        """
        Return dog object as string.

        :return: Dog
        """
        pass


class Toy:
    """Toy class."""

    def __init__(self, name: str, price: int):
        """
        Initialize toy object.

        :param name: Name
        :param price: Price
        """
        pass

    def __repr__(self) -> str:
        """
        Return yoy object as string.

        :return: Toy
        """
        pass


class Person:
    """Person class."""

    def __init__(self, name: str, money: int, preferences: list):
        """
        Initialize person object.

        :param name: Name
        :param money: Money
        :param preferences: Preferences in dog
        """
        pass

    def __repr__(self) -> str:
        """
        Return person object as string.

        :return: str.
        """
        pass

    def earn_money(self, earned: int):
        """
        Earn money for dog toys.

        :param earned: Earned amount
        """
        pass


class Shelter:
    """Shelter."""

    def __init__(self, money: int):
        """
        Initialize shelter object.

        :param money: Money
        """
        pass

    def buy_toys(self, toy: Toy) -> bool:
        """
        Buy toy for the shelter.

        Toy can be bought only if shelter has enough money.
        :param toy: Toy
        :return: boolean
        """
        pass

    def check_for_toys_available(self, dog: Dog) -> bool:
        """
        Check for available toys in the shelter.

        If all toys that dog needs are available, return True.
        If at least one toy that dog needs is not in shelter or is in shelter but is not available, return False.

        :param dog: Dog
        :return: boolean
        """
        pass

    def add_dog(self, dog: Dog):
        """
        Add dog to the shelter.

        Dog can be added to the shelter if all toys that it needs are in the shelter and are available.
        Add dog to the shelter.

        :param dog: Dog
        """
        pass

    def choose_dog(self, person: Person) -> Dog | None:
        """
        Choose the most suitable dog for the person.

        The most suitable dog is the one that has the most skills that person has in preferences.

        NB! If dog is an "introvert" and owner already gas a dog, it can not be chosen.
        If dog is an "extravert" and person does not have a dog already, it cant be chosen.

        Return the chosen dog if it is a match, else return None.

        :param person: Person that wants to choose dog
        :return: Dog if it was chosen, None if no match
        """
        pass

    def buy_dog_toys(self, dog: Dog, person: Person) -> bool:
        """
        Buy dog toys.

        The chosen dog has toys that it needs. You need to help the person to buy them from the shelter.

        You need to buy only those toys that belong to the dog person wants to adopt.
        Put all the toys that you need to buy together and check if person has enough money for it
        (person pays double price for each toy because shelter must receive profit)

        Return True and purchase the toys if it can be done, else return False.

        :param dog: Dog to buy toys for
        :param person: Person that must buy toys
        :return: boolean.
        """
        pass

    def adopt_dog(self, dog: Dog, person: Person) -> bool:
        """
        Adopt dog.

        Dog can be adopted only if person has the toys for it.

        Return True if adoption was successful, else return False.

        :param dog: Dog to adopt
        :param person: Person who adopts the dog
        :return: boolean
        """
        pass

    def sort_shelter_dogs(self) -> list[Dog]:
        """
        Sort all shelter dogs.

        Sort dogs by number of skills in descending order, if skills count is the same,
        sort by names alphabetically (a-z).

        :return: List of sorted dogs
        """
        pass

    def sort_shelter_toys(self) -> list[Toy]:
        """
        Sort all shelter toys.

        Sort shelter toys by price in descending order, if price is the same sort by names alphabetically (a-z).
        :return: List of sorted toys
        """
        pass


if __name__ == '__main__':
    # modify_string
    print(modify_string("12355ing"))  # walking
    print(modify_string("walking"))  # walking
    print(modify_string("walk"))  # walking
    print(modify_string("swimming"))  # swimmingly
    print(modify_string("go"))  # go
    print(modify_string("skiing"))  # skiingly

    # capitalize_first_last_letters
    print(capitalize_first_last_letters("python exercises practice solution"))  # PythoN ExerciseS PracticE SolutioN
    print(capitalize_first_last_letters("IAIB 2023 program"))  # IaiB 2023 PrograM
    #
    # # uno_game
    # print(uno_game(["yellow 3", "red 3"], "red 10"))  # Uno!
    # print(uno_game(["blue 1"], "blue 5"))  # Win!
    # print(uno_game(["blue 1", "green 2", "yellow 4", "red 2"], "blue 5"))  # Continue...
    #
    # # find_anagrams
    # print(find_anagrams(["listen", "silent", "hello", "person", "nosrep", "world", "nistel"]))
    # # {'listen': ['silent', 'nistel'],
    # # 'silent': ['listen', 'nistel'],
    # # 'nistel': ['listen', 'silent'],
    # # 'person': ['nosrep'],
    # # 'nosrep': ['person']}
    # print(find_anagrams(["hello", "hello"]))  # {}
    # print(find_anagrams(["hello", "hello", "Ohell"]))
    # # {'hello': ['ohell'], 'ohell': ['hello']}
    #
    # # count_layers
    # print(count_layers(""))  # 1
    # print(count_layers(('*\n'
    #                     '***\n'
    #                     '*****\n'
    #                     '*******\n'
    #                     '*********\n')))  # 6
    # print(count_layers(('n/*\n'
    #                     '/n***\n'
    #                     '/n*****\n'
    #                     '/n*******\n'
    #                     '/n*********\n'
    #                     '/n***********\n'
    #                     '/n*************\n')))  # 8
    #
    # # rhombus_pattern
    # print(rhombus_pattern(4, False))
    # # [
    # #     '   *   ',
    # #     '  ***  ',
    # #     ' ***** ',
    # #     '*******',
    # #     ' ***** ',
    # #     '  ***  ',
    # #     '   *   '
    # # ]
    # print(rhombus_pattern(4, True))
    # # [
    # #     '   *   ',
    # #     '  * *  ',
    # #     ' * * * ',
    # #     '* * * *',
    # #     ' * * * ',
    # #     '  * *  ',
    # #     '   *   '
    # # ]
    # print(rhombus_pattern(2, False))
    # # [
    # #     ' * ',
    # #     '***',
    # #     ' * '
    # # ]
    # print(rhombus_pattern(0, False))  # []
    #
    # # playlist
    # song1 = Song("Madness", "Muse", 101)
    # song2 = Song("tuju", "meelik", 102)
    # song3 = Song("Fine line", "harry styles", 377)
    # song4 = Song("madness", "Muse", 100)
    #
    # playlist = Playlist()
    # playlist.add_song(song1)
    # playlist.add_song(song2)
    # playlist.add_song(song3)
    # playlist.add_song(song4)
    # print(playlist.songs)
    # # ["Madness" by Muse, "Tuju" by Meelik, "Fine Line" by Harry Styles]
    #
    # print(playlist.get_duration_of_playlist())  # 580
    # print(playlist.get_longest_song())  # "Fine Line" by Harry Styles
    # print(playlist.get_songs_by_artist("MUSE"))  # ["Madness" by Muse]
    #
    # # dog shelter
    # # Shelter and adoption logic
    # shelter = Shelter(50)
    #
    # dog1 = Dog("muki", ["likes to play", "goes outside", "extravert"], ["ball", "frisbee"])
    # dog2 = Dog("polly", ["likes to play"], ["bone", "ball"])
    #
    # print(shelter.check_for_toys_available(dog1))  # False -> shelter does not have the toys for Muki
    #
    # ball = Toy("ball", 7)
    # frisbee = Toy("frisbee", 3)
    # bone = Toy("Bone", 4)
    #
    # shelter.buy_toys(ball)
    # shelter.buy_toys(frisbee)
    # shelter.buy_toys(bone)
    #
    # print(shelter.check_for_toys_available(dog1))  # True
    # shelter.add_dog(dog1)
    #
    # print(shelter.check_for_toys_available(dog2))  # False -> shelter has a ball, but it already belongs to Muki
    #
    # ball2 = Toy("ball", 7)
    # shelter.buy_toys(ball2)
    # shelter.check_for_toys_available(dog2)
    # shelter.add_dog(dog2)
    #
    # print(shelter.money)  # 29
    #
    # print(shelter.dogs)  # [Muki, Polly]
    #
    # person = Person("emili", 10, ["likes to play", "goes outside"])
    #
    # chosen_dog = shelter.choose_dog(person)
    # print(chosen_dog)
    # # Polly -> Muki has both skills that person is looking for, but it is extravert, so Emili cant take him,
    # # because Emili does not have any other dogs
    #
    # print(shelter.buy_dog_toys(chosen_dog, person))  # False, Emili does not have enough money
    # person.earn_money(30)
    # print(person.money)  # 40
    #
    # print(shelter.buy_dog_toys(chosen_dog, person))  # True
    # print(person.money)  # 18
    # print(shelter.money)  # 51
    # shelter.adopt_dog(chosen_dog, person)
    #
    # print(shelter.dogs)  # [Muki]
    # print(shelter.toys)
    #
    # # Sorting
    #
    # shelter2 = Shelter(110)
    #
    # bella = Dog("bella", ["likes to play", "goes outside", "extravert"],
    #             ["ball", "frisbee", "squishmallow"])
    # luna = Dog("lunA", ["likes to play", "introvert"], ["plush turtle", "ball"])
    # charlie = Dog("cHarlie", ["likes to play", "goes outside"], ["bacon"])
    #
    # ball3 = Toy("ball", 5)
    # frisbee2 = Toy("frIsBEE", 6)
    # squishmallow = Toy("squishmallow", 12)
    # plush_turtle = Toy("Plush turTle", 10)
    # ball4 = Toy("BalL", 5)
    # bacon = Toy("bAcOn", 3)
    # available_toy1 = Toy("available1", 15)
    # available_toy2 = Toy("available2", 3)
    # available_toy3 = Toy("available3", 7)
    #
    # shelter2.buy_toys(available_toy1)
    # shelter2.buy_toys(available_toy2)
    # shelter2.buy_toys(available_toy3)
    #
    # toys = [ball3, frisbee2, squishmallow, plush_turtle, ball4, bacon]
    # for i in toys:
    #     shelter2.buy_toys(i)
    # shelter2.add_dog(bella)
    # shelter2.add_dog(luna)
    # shelter2.add_dog(charlie)
    #
    # print(shelter2.sort_shelter_toys())
    # # [Available1, Squishmallow, Plush turtle, Available3, Frisbee, Ball, Ball, Available2, Bacon]
    # print(shelter2.sort_shelter_dogs())  # [Bella, Charlie, Luna]
