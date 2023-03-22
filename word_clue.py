"""WordClue class.

This program initializes an object with the word, its slices, and its clue. It
takes in a word and clue and gives a variety of functions of what do with those
inputs such as returning its slices, hints, and comparing two different
WordClue objects.

Author: Joseph Pogoretskiy
Version: 12/9/2022
Honor Code: All work is my own.
"""


from word_utilities import WordUtilities


class WordClue():
    """Word clue class.

    Attributes:
        word (str): Inputted word.
        clue (str): Inputted clue.

    """

    def __init__(self, word, clue):
        """Intialize a word with its clue.

        Args:
            word (str): Inputted word.
            clue (str): Inputted clue of the word.

        """
        MIN_WORD_LENGTH = 4
        MAX_CLUE_LENGTH = 40
        self.word_slices = []

        if (word is None) or (len(word) < MIN_WORD_LENGTH):
            self.word = "DEFAULT"
        else:
            self.word = word
        if (clue is None) or (len(clue) > MAX_CLUE_LENGTH) or (len(clue) < 1):
            self.clue = "DEFAULT CLUE"
        else:
            self.clue = clue

    def __eq__(self, other):
        """Check if two word attributes contain the same characters.

        Args:
            other (object): WordClue object being compared to.

        Returns:
            bool: Whether the two word attributes have the same characters.

        """
        self.word = self.word.upper()
        other.word = other.word.upper()
        if self.word == other.word:
            return True
        else:
            return False

    def get_clue(self):
        """Return the clue of the object.

        Returns:
            str: The word's clue.

        """
        return self.clue

    def get_first_letter_hint(self):
        """Return the first letter of the word.

        Returns:
            str: The word's first letter uppercased.

        """
        return self.word[0].upper()

    def get_first_slice_hint(self):
        """Return the first slice of the word.

        Returns:
            str: The word's first slice uppercased.

        """
        word_object = WordUtilities()
        self.word_slices = word_object.slicer(self.word)
        return self.word_slices[0]

    def get_whole_word_hint(self):
        """Return the whole word as a hint.

        Returns:
            str: The whole word.

        """
        return self.word.upper()

    def get_slices(self):
        """Return the slices of the word.

        Returns:
            list: Returns a list of WordSlice objects.

        """
        word_object = WordUtilities()
        self.word_slices = word_object.slicer(self.word)
        return self.word_slices

    def get_word(self):
        """Return the word.

        Returns:
            str: The whole word.

        """
        return self.word

    def __str__(self):
        """Return formatted information about the object.

        Returns:
            str: The word, clue, and a spaced list of the word's slices.

        """
        word_object = WordUtilities()
        self.word_slices = word_object.slicer(self.word)
        for i in range(len(self.word_slices)):
            self.word_slices[i] = str(self.word_slices[i])
        joined_slices = " ".join(self.word_slices)
        return f'{self.word}-{self.clue}\n{joined_slices}\n'
