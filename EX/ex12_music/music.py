"""Music."""
from __future__ import annotations


class Note:

    """
    Note class.
    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """
    def __init__(self, note: str):
        """Init the class"""
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

        result = "Notes:\n"
        if len(self.notes) > 0:
            for note_object in self.notes:
                result += " * " + note_object.note + "\n"
            result = result[:-1]
        else:
            result += "  Empty."
        return result


if __name__ == '__main__':
    note_one = Note('a')  # yes, lowercase
    note_two = Note('C')
    note_three = Note('Eb')
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

    collection = NoteCollection()
    # #
    # print(note_one)  # <Note: A>
    # print(note_three)  # <Note: Eb>
    #
    collection.add(note_one)
    collection.add(note_two)

    # collection2 = NoteCollection()
    # collection2.add(note_one)
    # print(collection2.extract())  # [<Note: A>,<Note: C>]
    # print(collection2.get_content())

    print(collection.get_content())
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
