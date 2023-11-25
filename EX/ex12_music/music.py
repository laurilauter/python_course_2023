"""Music."""
from __future__ import annotations


class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """

    def __init__(self, note: str):
        """Init the class."""
        note_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        note_letter = note[:1]
        alteration = note[1:2]

        if note_letter.isalpha() and alteration:
            if alteration.lower() == "b":
                index = note_letters.rfind(note_letter.upper())
                if index >= 1:
                    previous_char = note_letters[index - 1]
                    self.note = previous_char + "#"
                else:
                    self.note = "Z#"
            elif alteration.lower() == "#":
                self.note = note_letter.upper() + "#"
        else:
            self.note = note_letter.upper()

        """Initialize the class.
        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note}>"

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        return type(other) is self.__class__ and self.note == other.note


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """
        self.notes = []

    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """
        if not isinstance(note, Note):
            raise TypeError("note must be a Note instance")
        if note not in self.notes:
            self.notes.append(note)

    def pop(self, note: str) -> Note | None:
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        note_object = Note(note)
        removed_note = None
        if note_object in self.notes:
            index = self.notes.index(note_object)
            removed_note = self.notes.pop(index)
        return removed_note

    def extract(self) -> list[Note]:
        """
        Return a list of all the notes from the collection and empty the collection itself.

        Order of the list must be the same as the order in which the notes were added.

        Example:
          collection = NoteCollection()
          collection.add(Note('A'))
          collection.add(Note('C'))
          collection.extract() # -> [<Note: A>, <Note: C>]
          collection.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted everything.

        :return: A list of all the notes that were previously in the collection.
        """
        extraction_result = []
        if self.notes:
            extraction_result = self.notes
            self.notes = []
        return extraction_result

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the collection.

        Example:
          collection = NoteCollection()
          collection.add(Note('C', '#'))
          collection.add(Note('L', 'b'))
          print(collection.get_content())

        Output in console:
           Notes:
            * C#
            * Lb

        The notes must be sorted alphabetically by name and then by sharpness, that is A, A#, B, Cb, C and so on.
        Recommendation: Use normalized note names, not just the __repr__()

        :return: Content as a string
        """
        sorted_notes = sorted(self.notes, key=lambda note_obj: (note_obj.note[:1], note_obj.note[1:2]))
        result = "Notes:\n"
        if len(sorted_notes) > 0:
            for note_object in sorted_notes:
                result += "  * " + note_object.note + "\n"
            result = result[:-1]
        else:
            result += "  Empty."
        return result


#  2nd part CHORDS

class Chord:
    """Chord class."""

    def __init__(self, note_one: Note, note_two: Note, chord_name: str, note_three: Note = None):
        """
        Initialize chord class.

        A chord consists of 2-3 notes and their chord product (string).
        If any of the parameters are the same, raise the 'DuplicateNoteNamesException' exception.
        """
        self.chord_name = chord_name
        self.chord_notes = []
        note_list = [note_one, note_two, note_three]

        for n in note_list:
            if isinstance(n, Note) and n.note not in self.chord_notes:
                print(f"not in list {n.note}", n.note not in self.chord_notes)
                self.chord_notes.append(n.note)
        print("c1", len(self.chord_notes) < 2)
        print("c2", len(self.chord_notes) != len(set(self.chord_notes)))
        print("c3", chord_name in self.chord_notes)
        if len(self.chord_notes) < 2 or len(self.chord_notes) != len(set(self.chord_notes)) or \
                chord_name in self.chord_notes:
            raise DuplicateNoteNamesException("Chord notes must be different and also differ from chord name.")

    def __repr__(self) -> str:
        """
        Chord representation.

        Return as: <Chord: [chord_name]> where [chord_name] is the name of the chord.
        """
        return f"<Chord: {self.chord_name}>"


class Chords:
    """Chords class."""

    def __init__(self):
        """
        Initialize the Chords class.

        Add whatever you need to make this class function.
        """

    def add(self, chord: Chord) -> None:
        """
        Determine if chord is valid and then add it to chords.

        If there already exists a chord for the given pair of components, raise the 'ChordOverlapException' exception.

        :param chord: Chord to be added.
        """

    def get(self, first_note: Note, second_note: Note, third_note: Note = None) -> Chord | None:
        """
        Return the chord for the 2-3 notes.

        The order of the first_note and second_note and third_note is interchangeable.

        If there are no combinations for the 2-3 notes, return None

        Example:
          chords = Chords()
          chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
          print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
          print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
          print(chords.get(Note('D'), Note('Z')))  # ->  None
          chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
          print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

        :param first_note: The first note of the chord.
        :param second_note: The second note of the chord.
        :param third_note: The third note of the chord.
        :return: Chord or None.
        """
        return None


class DuplicateNoteNamesException(Exception):
    """Raised when attempting to add a chord that has same names for notes and product."""


class ChordOverlapException(Exception):
    """Raised when attempting to add a combination of notes that are already used for another existing chord."""


if __name__ == '__main__':
    # note_one = Note('a')  # yes, lowercase
    # note_two = Note('C')
    # note_three = Note('Eb')
    # print(note_one)
    # print(note_two)
    # print(note_three)

    # note_4 = Note('A#')
    # note_5 = Note('Bb')
    # note_6 = Note('Cb')
    # print(note_4)
    # print(note_5)
    # print(note_6)
    #
    # print(note_4 == note_5)

    # print(note_one)

    # collection = NoteCollection()
    # #
    # print(note_one)  # <Note: A>
    # print(note_three)  # <Note: Eb>
    #
    # collection.add(note_one)
    # collection.add(note_two)

    # collection2 = NoteCollection()
    # collection2.add(note_one)
    # print(collection2.extract())  # [<Note: A>,<Note: C>]
    # print(collection2.get_content())

    # print(collection.get_content())
    # Notes:
    #   * A
    #   * C
    #
    # print(collection.extract())  # [<Note: A>,<Note: C>]
    # print(collection.get_content())
    # # Notes:
    # #  Empty
    #
    # collection.add(note_one)
    # collection.add(note_two)
    # collection.add(note_three)
    #
    # # print(collection.pop('a') == note_one)  # True
    # # print(collection.pop('Eb') == note_three)  # True
    #
    # print(collection.pop('a'))  #

    # chords = Chords()
    # chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    # print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
    # print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
    # print(chords.get(Note('D'), Note('Z')))  # ->  None
    # chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
    # print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

    # chords = Chords()
    #
    # chord1 = Chord(Note('A'), Note('C#'), 'Amaj', Note('E'))
    # chord2 = Chord(Note('E'), Note('G'), 'Emin', note_three=Note('B'))
    # chord3 = Chord(Note('E'), Note('B'), 'E5')
    # chord_bad1 = Chord(Note('B'), Note('B'), 'E1', Note('B'))
    chord_bad2 = Chord(Note('A'), Note('A'), 'C', Note('D'))
    # chord_bad3 = Chord(Note('E'), Note('B'), 'E3')
    # chord_bad4 = Chord(Note('E'), Note('B'), 'E4')
    # print(chord1)
    # print(chord2)
    # print(chord3)
    # print(chord_bad1)
    print(chord_bad2)
    # print(chord_bad3)
    # print(chord_bad4)
    #
    # chords.add(chord1)
    # chords.add(chord2)
    # chords.add(chord3)
    #
    # print(chords.get(Note('e'), Note('b')))  # -> <Chord: E5>
    #
    # try:
    #     wrong_chord = Chord(Note('E'), Note('A'), 'E')
    #     print('Did not raise, not working as intended.')
    # except DuplicateNoteNamesException:
    #     print('Raised DuplicateNoteNamesException, working as intended!')

    # try:
    #     chords.add(Chord(Note('E'), Note('B'), 'Emaj7add9'))
    #     print('Did not raise, not working as intended.')
    # except ChordOverlapException:
    #     print('Raised ChordOverlapException, working as intended!')
