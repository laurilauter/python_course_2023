"""Exam 3 (2024-01-09)."""
from __future__ import annotations

import math


def create_new_string(text: str) -> str:
    """
    Create a new string from the first 2 and last 2 characters of the given string.

    If the input string has a length of less than 2, it returns an empty string.
    If the input string has a length of 2, it returns the input string.
    If the input string has a length of 3, then the middle symbol is used only once.

    Example:
    create_new_string("Python") -> Pyon
    create_new_string("Hi") -> Hi
    create_new_string("A") -> ''
    create_new_string("") -> ''
    create_new_string("aba") -> 'aba'

    :param text: The input string from which the new string will be created.
    :return: A new string containing the first 2 and last 2 characters of the input string.
    """
    result = ""
    if len(text) > 3:
        return text[:2] + text[-2:]
    elif len(text) >= 2:
        return text
    return result


def first_repeated_word(str1) -> str:
    """
    Take a string and finds the first recurring word in that string.

    :param str1: Input text in which the first recurring word is being searched.
    :return: The first recurring word, or 'None' if there are no recurring words.
    """
    words = str1.split(" ")
    for word in words:
        if words.count(word) > 1:
            return word
    return "None"


def find_consecutive_sublists(numbers: list) -> list:
    """
    Find all consecutive sublists in a list of numbers.

    All the consecutive numbers, have to be in the same sublist.
    Numbers in list are always increasing.

    For example:
    find_consecutive_sublists([1, 2, 3, 5, 6, 7]) => [[1, 2, 3], [5, 6, 7]]
    find_consecutive_sublists([4, 6, 8]) => [[4], [6], [8]]
    find_consecutive_sublists([2, 4, 8, 9, 10]) => [[2], [4], [8, 9, 10]]
    find_consecutive_sublists([]) => []
    """
    result = []
    sublist = []
    for i in range(len(numbers)):
        if i == 0 or numbers[i] - numbers[i - 1] != 1:
            if sublist:
                result.append(sublist)
            sublist = [numbers[i]]
        else:
            sublist.append(numbers[i])
    if sublist:
        result.append(sublist)

    return result


def average_word_length(words: dict):
    """
    Find the average length of the words in the lists corresponding to the even-numbered keys.

    The function receives the input of the dictionary, where the keys are integers and the values are lists of words.

    The answer must be a whole number, i.e. round up if necessary.

    average_word_length({2: ["awesome"]}) => 7
    average_word_length({13: ["awesome"]}) => 0
    average_word_length({0: ["a", "b", "c"], 2: ["aa", "bb", "cc"], 6: ["aaa", "bbb", "ccc"]}) => 2

    :param words: given dictionary of integers as keys and lists of words as values
    :return: average word length as an integer
    """
    int_result = 0
    even_keys = []

    for key in words.keys():
        if key % 2 == 0:
            even_keys.append(key)
    words_list = []
    for key in even_keys:
        words_list += words[key]

    word_lengths = []
    for word in words_list:
        word_lengths.append(len(word))

    if len(word_lengths) == 0:
        return int_result

    result = sum(word_lengths) / len(word_lengths)

    decimals = 0
    multiplier = 10 ** decimals
    return math.ceil(result * multiplier) / multiplier


def count_pythons(text, letter_counts=None) -> int:
    """
    Count how many times "python" can be spelled.

    Count the letters 'p', 'y', 't', 'h', 'o', and 'n'
    to spell the word 'python' using the letters from the given text.
    Method must be case-insensitive.
    Use recursion!

    count_pythons("It is a programming language") => 0
    count_pythons("Python, pYthoN parapapython") => 3
    count_pythons("In python we use dictionary to store data") => 1
    count_pythons("On the porch was hot and sunny") => 1

    :param text: The input text to analyze.
    :param letter_counts: A parameter to track the counts of each letter.
    :return: The number of times the word 'python' can be formed using the collected letters in the text.
    """
    count = 0
    if letter_counts:
        count = letter_counts

    text = text.lower()
    python = "python"

    for char in text:
        if char in python:
            text = text.replace(char, "", 1)
            python = python.replace(char, "")
            if not python:
                count += 1
                return count_pythons(text) + count
    return count


def increasing_subsequences(nums: list, count: int) -> list or str:
    """
    Find strictly increasing subsequences in a given list.

    Find increasing subsequences. Minimal length of subsequence is 2.

    The result has to contain the list of tuples, where first element is increasing subsequence,
    and second element is length of subsequence. The amount of the subsequences in result has to be equal
    to parameter count. If count is bigger than amount of subsequences, return 'Not enough subsequences!'.

    :param nums: The input list of integers.
    :param count: The number of subsequences to find.
    :return: list: A list of tuples, each containing a subsequence and its length.

    Examples:
    increasing_subsequences([1, 3, 5, 2, 7, 8, 0], 2)  -> [([1, 3, 5], 3), ([2, 7, 8], 3)]
    increasing_subsequences([10, 9, 5, 1, 3, 4, 2, 6, 8], 2) -> [([1, 3, 4], 3), ([2, 6, 8], 3)]
    increasing_subsequences([1, 2, 4, 3], 2) -> "Not enough subsequences!"
    increasing_subsequences([1, 2, 4, 0], 0) -> []
    """

    if not count or not nums or count == 0:
        return []

    subsequences = []
    i = 0
    while i < len(nums) - 1:
        subsequence = [nums[i]]
        for j in range(i + 1, len(nums)):
            if nums[j] > subsequence[-1]:
                subsequence.append(nums[j])
                if j + 1 == len(nums):
                    subsequences.append((subsequence, len(subsequence)))
                    i = j
            elif len(subsequence) > 1 or j == len(nums) - 1:
                subsequences.append((subsequence, len(subsequence)))
                i = j
                break
            else:
                subsequence = [nums[j]]
                i = j

    is_equal_length = True

    if len(subsequences) < count or not is_equal_length or len(subsequences) == 1:
        return "Not enough subsequences!"
    elif not count or not nums or count == 0:
        return []
    else:
        return subsequences[:count]


class Movie:
    """Movie class."""

    def __init__(self, title: str, genre: str, starting_in: float):
        """
        Initialize Movie.

        :param title: title of movie
        :param genre: genre of movie
        :param starting_in: hours until movie airs
        """

        self.title = title.title()
        self.genre = genre.lower()
        self.starting_in = starting_in


class Cinema:
    """Cinema class."""

    def __init__(self):
        """Initialize Cinema."""
        self.movies = []

    def add_movie(self, movie: Movie):
        """
        Add Movie to Cinema.

        :param movie: Movie object
        """
        self.movies.append(movie)

    def can_remove_movie(self, movie: Movie) -> bool:
        """
        Check if movie is in Cinema.

        :return: boolean
        """
        if movie in self.movies:
            return True
        return False

    def remove_movie(self, movie: Movie):
        """
        Remove movie from Cinema.

        :param movie: Movie object
        """
        self.movies.remove(movie)

    def get_movies_by_genre(self, genre: str) -> list[Movie]:
        """
        Return list of movies with given genre.

        :param genre:
        :return:
        """
        result = []
        for movie in self.movies:
            if movie.genre.lower() == genre.lower():
                result.append(movie)
        return result

    def get_genre_of_movie_with_title(self, title: str) -> str:
        """
        Get the genre of movie with given title.

        If no such movie is in Cinema, return "No such movie".

        :param title: name of movie
        :return: genre
        """
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie.genre
        return "No such movie"

    def get_movie_timetable(self) -> list[Movie]:
        """
        Return list of movies in order of airing soonest.

        :return: list of movies
        """
        return sorted(self.movies, key=lambda movie: movie.starting_in)

    def get_next_airing(self) -> str:
        """
        Return title of movie that airs next in cinema.

        :return: title of movie
        """
        next_m = sorted(self.movies, key=lambda movie: movie.starting_in)
        return next_m[0].title

    def get_movies(self) -> list[Movie]:
        """Return movie list."""
        return self.movies


class Song:
    """Song."""

    def __init__(self, name: str, genre: str, duration: float, difficulty: int):
        """
        Song object initialization.

        :param name: Song name.
        :param genre: Song genre.
        :param duration: Song duration.
        :param difficulty: Song difficulty.
        """
        self.name = name
        self.genre = genre
        self.duration = duration
        self.difficulty = difficulty
        if difficulty > 10:
            self.difficulty = 10
        elif difficulty < 1:
            self.difficulty = 1

    def __repr__(self):
        """
        Return song.

        :return: String in format "{name}, style: {genre}".
        """
        return f"{self.name}, style: {self.genre}"


class Contestant:
    """Contestant class."""

    def __init__(self, first_name: str, last_name: str, age: int, vocals: float):
        """
        Contestant object initialization.

        :param first_name: First name.
        :param last_name: Last name.
        :param age: Age.
        :param vocals: Vocals.
        """
        self.name = first_name.capitalize() + " " + last_name.capitalize()
        self.age = int(age)
        self.vocals = vocals
        self.favorite_song = None

    def __repr__(self):
        """
        Return contestant.

        :return: String with full name.
        """
        return f"{self.name}"

    def choose_song(self, song_list: list[Song]) -> Song | None:
        """
        Choose song for the competition.

        Chosen song name must contain the most characters from the contestant full name.
        If there are no songs which contain at least one character of contestant's name, return None.

        If the contestant name is "ABC"
        Then
        "EFG" - would not match at all
        "ABC" and "ABCABC" and "CCAAB" have the most matches (all 3 characters from the name)
        "ABU ABBA" and "Baaky" have 2 matching characters.

        If multiple songs have the same number of matching characters, then any song is suitable
        (meaning it doesn't matter which one to choose - the first one is ok).

        :param song_list: List of songs to chose from.
        :return: Contestants song or None.
        """
        match_count = []
        max_song = []
        match_score = 0
        name_letters = self.name.lower()
        for song in song_list:
            count = 0
            name = song.name
            for letter in name_letters:
                if letter in name:
                    count += 1
                    name.replace(letter, "")
            if count > 0:
                match_count.append((song, count))

        for song in match_count:
            if song[1] > match_score:
                max_song = [song[0]]

        if not max_song:
            return None

        self.favorite_song = max_song[0]
        return max_song[0]


class Judge:
    """Judge."""

    def __init__(self, name: str, preferences: list[str]):
        """
        Judge object initialization.

        :param name: Name.
        :param preferences: Preferences.
        """
        self.name = name.title()
        self.preferences = preferences

    def __repr__(self):
        """
        Return judge.

        :return: String with judge name.
        """
        return self.name


class Competition:
    """Competition."""

    def __init__(self, minimum_age: int, maximum_age: int, suitable_genres: list):
        """
        Competition object initialization.

        :param minimum_age: Maximum age.
        :param maximum_age: Minimum age.
        :param suitable_genres: Suitable genres.
        """
        self.minimum_age = minimum_age
        self.maximum_age = maximum_age
        self.suitable_genres = suitable_genres
        self.contestants = []
        self.judges = []

    def add_contestant(self, contestant: Contestant) -> bool:
        """
        Register contestant.

        Can be registered if is Contestant and age and chosen song genre is allowed on the competition.

        :param contestant: Contestant.
        :return: Boolean.
        """
        if not isinstance(contestant, Contestant):
            return False

        genre = None
        try:
            song = contestant.choose_song()
            if song is not None:
                genre = song.genre
        except Exception:
            pass

        if self.minimum_age < contestant.age < self.maximum_age and genre in self.suitable_genres:
            self.contestants.append(contestant)
            return True

    def add_judge(self, judge: Judge) -> bool:
        """
        Add judge to the competition.

        Can be added only in case if he/she is Judge and likes the same genres that are allowed on the competition.
        All the judge's genres have to be allowed.

        :param judge: Judge.
        :return: Boolean.
        """
        # for genre in self.suitable_genres:
        #     if isinstance(judge, Judge):
        #         for judge_genre in judge.preferences:
        #             if genre == judge_genre:
        #                 self.judges.append(judge)
        #                 return True

        if isinstance(judge, Judge):
            for judge_genre in judge.preferences:
                for genre in self.suitable_genres:
                    if judge_genre.lower() != genre.lower():
                        break
                    self.judges.append(judge)
                    return True
        return False

    def create_order_of_performances(self) -> list[Contestant]:
        """
        Create order of performances.

        First ones to perform are the youngest. In case of same age, alphabetically by song name.

        :return: Order of performances.
        """
        # half done
        return sorted(self.contestants, key=lambda contestant: contestant.age, reverse=True)

    def perform_song_rankings(self) -> dict:
        """
        Create ranking chart where key is song and value is ranking.

        Ranking = song difficulty * contestant vocals + 10 if judge likes that genre.

        :return: Rankings
        """
        rankings = {}
        for contestant in self.contestants:
            judge_like = 0
            for judge in self.judges:
                if contestant.favorite_song.genre in judge.preferences:
                    judge_like = 10
            rankings[contestant.favorite_song] = contestant.favorite_song.difficulty * contestant.vocals + judge_like

        return rankings

    def get_suitable_genres(self) -> list:
        """
        Sort competition genres by name (a-z).

        :return: Sorted genres.
        """
        sorted(self.suitable_genres, key=lambda genre: genre, reverse=True)

    def get_contestants(self) -> list:
        """
        Sort contestants by names (a-z).

        :return: Sorted contestants.
        """
        return sorted(self.contestants, key=lambda contestant: contestant.name)

    def get_judges(self) -> list:
        """
        Sort Judges by names (a-z).

        :return: Sorted judges.
        """
        return sorted(self.judges, key=lambda judge: judge.name)

    def get_judges_rankings_in_order(self) -> list[Song]:
        """
        Sort songs by judges rankings from best to worst.

        :return: Sorted songs.
        """
        return sorted(self.judges, key=lambda judge: judge.name)

    def get_winner(self) -> Song:
        """
        Return winner song by judges ranking.

        :return: Winner song.
        """
        return sorted(self.judges, key=lambda judge: judge.name)


if __name__ == '__main__':
    # create_new_string
    # print(create_new_string("Python"))  # "Pyhon"
    # print(create_new_string("Hi"))  # "Hi"
    # print(create_new_string("A"))  # ''
    # print(create_new_string(""))  # ''
    # print(create_new_string("aba"))  # ''
    #
    # # first_repeated_word
    # print(first_repeated_word("ab ca bc ab"))  # ab
    # print(first_repeated_word("ab ca bc ab ca ab bc"))  # ab
    # print(first_repeated_word("ab ca bc ca ab bc"))  # ab
    # print(first_repeated_word("ab ca bc"))  # None
    #
    # # find_consecutive_sublists
    # print(find_consecutive_sublists([1, 2, 3, 5, 6, 7]))
    # # => [[1, 2, 3], [5, 6, 7]]
    # print(find_consecutive_sublists([4, 6, 8]))
    # # => [[4], [6], [8]]
    # print(find_consecutive_sublists([2, 4, 8, 9, 10]))
    # # => [[2], [4], [8, 9, 10]]
    # print(find_consecutive_sublists([]))
    # # => []
    #
    # # average_word_length
    # print(average_word_length({2: ["awesome"]}))  # => 7
    # print(average_word_length({13: ["awesome"]}))  # => 0
    # print(average_word_length({0: ["a", "b", "c"], 2: ["aa", "bb", "cc"], 6: ["aaa", "bbb", "ccc"]}))  # => 2
    # print(average_word_length({0: ["123456789012345678901234567890123456789012345678901", "12345678901234567890123456789012345678901234567890"]}))  # => 2

    # count_pythons
    # print(count_pythons("Ihj pYthoN pYthoN"))  # => 2
    # print(count_pythons("It is a programming language"))  # => 0
    # print(count_pythons("Python, pYthoN parapapython"))  # => 3
    # print(count_pythons("In python we use dictionary to store data"))  # => 1
    # print(count_pythons("On the porch was hot and sunny"))  # => 1

    # # increasing_subsequences
    # print(increasing_subsequences([1, 3, 5, 2, 7, 8, 0], 2))  # [([1, 3, 5], 3), ([2, 7, 8], 3)]
    # print(increasing_subsequences([10, 9, 5, 1, 3, 4, 2, 6, 8], 2))  # [([1, 3, 4], 3), ([2, 6, 8], 3)]
    # print(increasing_subsequences([1, 2, 4, 3], 2))  # "Not enough subsequences!"
    # print(increasing_subsequences([1, 2, 4, 0], 0))  # []
    # print(increasing_subsequences([1, 2, 4, 0, 7, 9, 10], 2))  # []
    # print(increasing_subsequences([1, 2, 10], 0))  # []
    # print(increasing_subsequences([], 0))  # []
    # print(increasing_subsequences([], 3))  # []
    # Cinema

    # cinema = Cinema()
    #
    # movie1 = Movie("inception", "Sci-Fi", 1.5)
    # movie2 = Movie("The Shawshank Redemption", "Drama", 2.0)
    # movie3 = Movie("Jurassic Park", "Adventure", 1.0)
    # movie4 = Movie("Jurassic Park 3", "Action", 1.0)
    #
    # cinema.add_movie(movie1)
    # cinema.add_movie(movie2)
    # cinema.add_movie(movie3)
    # cinema.add_movie(movie4)
    #
    # all_movies = cinema.get_movies()
    # print([movie.title for movie in all_movies])  # ['Inception', 'The Shawshank Redemption', 'Jurassic Park']
    #
    # cinema.remove_movie(movie2)
    #
    # drama_movies = cinema.get_movies_by_genre("Drama")
    # print([movie.title for movie in drama_movies])  # []
    # drama_movies = cinema.get_movies_by_genre("action")
    # print([movie.title for movie in drama_movies])  # []
    #
    # # genre_of_inception = cinema.get_genre_of_movie_with_title("Inception")
    # # print(genre_of_inception)  # sci-fi.
    # genre_of_inception = cinema.get_genre_of_movie_with_title("Jurassic Park 3")
    # print(genre_of_inception)  # action
    #
    # movie_timetable = cinema.get_movie_timetable()
    # print([movie.title for movie in movie_timetable])  # ['Jurassic Park', 'Inception']
    #
    # next_airing_movie = cinema.get_next_airing()
    # print({next_airing_movie})  # Jurassic Park

    # Song contest
    song1 = Song("Best day ever", "rock", 3.5, 15)
    song2 = Song("My enemy hair", "pop", 2.0, 5)
    song3 = Song("Kinda normal", "pop", 3.0, 7)
    song4 = Song("S1", "pop", 3.0, 7)
    song_list = [song1, song2, song3, song4]
    #song_list = [song4]

    bob = Contestant("bob", "Ernest", 20, 9)
    mari = Contestant("mari", "riisa", 9, 0)
    kiur = Contestant("Kiur", "norman", 15, 6)

    competition = Competition(10, 35, ["rock", "pop"])

    judge1 = Judge("Judy", ["Rock"])
    judge2 = Judge("emili", ["rock", "pop"])

    #  Choosing songs for competition
    print(bob.choose_song(song_list))  # Best day ever, style: rock
    print(mari.choose_song(song_list))  # My enemy hair, style: pop
    print(kiur.choose_song(song_list))  # Kinda normal, style: pop

    #  Register to competition
    print(competition.add_contestant(bob))  # True
    print(competition.add_contestant(mari))  # False
    print(competition.add_contestant(kiur))  # True

    #  Add judge to competition
    print(competition.add_judge(judge1))  # False
    print(competition.add_judge(judge2))  # True

    print(competition.create_order_of_performances())
    # [Kiur Norman, Bob Ernest]

    print(competition.perform_song_rankings())
    # {Best day ever, style: rock: 100, Kinda normal, style: pop: 52}

    print(competition.get_suitable_genres())  # ['pop', 'rock']

    print(competition.get_contestants())  # [Bob Ernest, Kiur Norman]

    print(competition.get_judges())  # [Emili]

    print(competition.get_judges_rankings_in_order())
    # [Best day ever, style: rock, Kinda normal, style: pop]

    print(competition.get_winner())  # Best day ever, style: rock
