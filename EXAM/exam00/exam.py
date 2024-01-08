"""Exam0."""
from typing import Optional
import re


def find_capital_letters(s: str) -> str:
    """
    Return only capital letters from the string.

    #1

    If there are no capital letters, return empty string.
    The string contains only latin letters (a-z and A-Z).
    The letters should be in the same order as they appear in the input string.

    find_capital_letters("ABC") => "ABC"
    find_capital_letters("abc") => ""
    find_capital_letters("aAbBc") => "AB"
    """
    result = ""
    for char in s:
        if char.isupper():
            result += char
    return result


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #2

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """

    nums = [abs(a), abs(b), abs(c)]
    nums.sort()

    if 0 <= nums[1] - nums[0] <= 1 < nums[2] - nums[1]:
        return True
    if 0 <= nums[2] - nums[1] <= 1 < nums[1] - nums[0]:
        return True
    return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #3

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    persons = results_string.split(",")
    structured_persons = []
    result = []
    for person in persons:
        parts = person.split(" ")
        if len(parts) > 1:
            score = parts[len(parts) - 1]
            parts.remove(parts[len(parts) - 1])
            name = " ".join(parts)
            if score.isnumeric():
                structured_persons.append([name, score])

    for person in structured_persons:
        if int(person[1]) >= min_result:
            if person[0]:
                result.append(person[0])

    return result


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #4

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1

    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2
    [2, 2, 2]
    [0, 2, 0]
    [0, 1, 0]

    :param game
    :return: winning player id
    """
    # rows
    for i in range(3):
        if game[i][0] > 0 and game[i][0] == game[i][1] == game[i][2]:
            return game[i][0]
    # cols
    if game[1][0] > 0 and game[1][0] == game[0][0] == game[2][0]:
        return game[1][0]
    elif game[1][1] > 0 and game[1][1] == game[0][1] == game[2][1]:
        return game[1][1]
    elif game[1][2] > 0 and game[1][2] == game[0][2] == game[2][2]:
        return game[1][2]
    # x
    elif game[1][1] > 0 and game[1][1] == game[0][0] == game[2][2]:
        return game[1][1]
    elif game[1][1] > 0 and game[1][1] == game[0][2] == game[2][0]:
        return game[1][1]
    else:
        return 0


def rainbows(field: str, lower=False) -> int:
    """
    Count rainbows.

    #5

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1  # Lisaks vikerkaarele on veel sümboleid
    assert rainbows("WoBniar") == 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    assert rainbows("rainbowobniar") == 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    field = field.lower()
    count = 0
    word = "rainbow"

    if word not in field and word[::-1] not in field:
        return count
    else:
        count += 1
        if word in field:
            field = field.replace(word,"",1)
        else:
            field = field.replace(word[::-1], "", 1)
        return count + rainbows(field)


def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #6

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    max_word = []

    for p in range(len(text)):
        word = ""
        for i in range(p, len(text) + 1):
            i = i + p
            if text[i:i + 1].lower() not in word:
                word += text[i:i + 1]
            else:
                if len(word) > len(max_word):
                    max_word.append(word)
                    word = ""
                    p += 1
    return max(max_word, key=len)


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Initialize student."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    avg_grade = 0
    if len(grades) > 0:
        avg_grade = round(sum(grades) / len(grades), 3)
    return Student(name, avg_grade, credit_points)


def get_top_student_with_credit_points(students: list, min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    top_student = Student("Dummy", 0, 0)
    top_students = [student for student in students if float(student.average_grade) >= float(min_credit_points)]

    for student in top_students:
        if top_student.average_grade < student.average_grade:
            top_student = student
        return top_student
    return None


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    pass


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    pass


class Room:
    """Room."""

    def __init__(self, number: int, price: int):
        """Initialize room."""
        pass

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        pass

    def get_features(self) -> list:
        """Return all the features of the room."""
        pass

    def get_price(self) -> int:
        """Return the price."""
        pass

    def get_number(self) -> int:
        """Return the room number."""
        pass


class Hotel:
    """Hotel."""

    def __init__(self):
        """Initialize hotel."""
        pass

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise add the room to hotel and return True.
        """
        pass

    def book_room(self, required_features: list) -> Optional[Room]:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        pass

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        pass

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        pass

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        pass

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        pass

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        pass


if __name__ == '__main__':

    # print(find_capital_letters("ABC")) # = > "ABC"
    # print(find_capital_letters("abc")) #= > ""
    # print(find_capital_letters("aAbBc")) #= > "AB"

    # print(close_far(1, 2, 10))
    # print(close_far(1, 2, 3))
    # print(close_far(4, 1, 3))
    # print(close_far(1, 20, 100)) # false
    # print(close_far(-4, -2, -1))  # false


    # print(get_names_from_results("ago 123,peeter 11", 0)) #  = > ["ago", "peeter"]
    # print(get_names_from_results("ago 123,peeter 11,33", 10)) #  = > ["ago", "peeter"]  # 33 does not have the name
    # print(get_names_from_results("ago 123,peeter 11", 100)) #  = > ["ago"]
    # print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11)) #  = > ["ago", "peeter", "kitty11!!"]
    # print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12)) #  = > ["ago", "kusti riin"]
    # print(get_names_from_results("tyu sdf123,3 11as,33", 10))
    # print(get_names_from_results("ti tim12345 34,9POrw2n1ll2gVXkA 8HNiBrBZ74S WYT...mHTvUk2X99S 35", 10))

    # print(tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]])) # = > 1
    # print(tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]])) # = > 0
    # print(tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]])) # = > 2
    # print(tic_tac_toe([[2, 1, 2], [1, 1, 2], [2, 2, 1]]))  # = > 0
    # print(tic_tac_toe([[0, 0, 0], [1, 1, 1], [0, 0, 0]])) # 1
    # print(tic_tac_toe([[0, 1, 0], [0, 1, 0], [0, 1, 0]])) # 1
    # print(tic_tac_toe([[0, 0, 1], [0, 0, 1], [0, 0, 1]]))# 1
    # print(rainbows("rainbowThisIsJustSomeNoise")) #  == 1  # Lisaks vikerkaarele on veel sümboleid
    # print(rainbows("WoBniar")) #  == 1  # Vikerkaar on tagurpidi ja sisaldab suuri tähti
    # print(rainbows("rainbowobniar")) #  == 1  # Kaks vikerkaart jagavad tähte seega üks neist ei ole valiidne

    # print(longest_substring("aaa"))# a
    # print(longest_substring("abc"))# abc
    # print(longest_substring("abccba"))# abc
    # print(longest_substring("babcdEFghij"))# abcdEFghij
    # print(longest_substring("abBcd"))# Bcd
    # print(longest_substring('aababcabcdabcdeabcdefabcdefgqwertyuiop')) # fgqwertyuiop

    low = create_student("Low", [1, 2, 1, 1], 4)
    mid = create_student("Mid", [2, 3, 3, 3], 4)
    high = create_student("High", [5, 5, 4, 5], 4)
    # print(dude.average_grade)
    print(get_top_student_with_credit_points([low, mid, high], 3))

    # hotel = Hotel()
    # room1 = Room(1, 100)
    # room1.add_feature("tv")
    # room1.add_feature("bed")
    # room2 = Room(2, 200)
    # room2.add_feature("tv")
    # room2.add_feature("sauna")
    # hotel.add_room(room1)
    # hotel.add_room(room2)
    # #  try to add room with existing number, try to add existing feature to room
    # assert hotel.get_rooms() == [room1, room2]
    # assert hotel.get_booked_rooms() == []
    #
    # assert hotel.book_room(["tv", "president"]) == room1
    # assert hotel.get_available_rooms() == [room2]
    # assert hotel.get_booked_rooms() == [room1]
    #
    # assert hotel.book_room([]) == room2
    # assert hotel.get_available_rooms() == []
    #
    # assert hotel.get_feature_profits() == {
    #     'tv': 300,
    #     'bed': 100,
    #     'sauna': 200
    # }
    # assert hotel.get_most_profitable_feature() == 'tv'
    #
    # #  try to add a room so that two or more features have the same profit
