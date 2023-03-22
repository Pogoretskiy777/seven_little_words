"""GameInfo class.

This program reads a file and initializes its words, clues, and its slices into
a variety of objects from other classes.

Author: Joseph Pogoretskiy
Version: 12/9/2022
Honor Code: All work is my own.
"""


from word_utilities import WordUtilities
from word_clue import WordClue
from file_utilities import FileUtilities


class GameInfo:
    """Word clue class.

    Attributes:
        filename (txt): A plain text file containing words and their clues.

    """

    def __init__(self, filename):
        """Initialize the provided file.

        Reads the information from the given file and constructs WordClue
        objects from each line along with WordSlice objects from each word.

        Args:
            filename (txt): A plain text file containing words and their clues.

        """
        NUMBER_OF_WORDS = 7
        self.filename = filename
        self.word_slices = []
        self.cluelist = []
        all_lines = FileUtilities.read_lines_from_file(self.filename,
                                                       NUMBER_OF_WORDS)
        if all_lines is None:
            self.complete = False
        elif (len(all_lines) > NUMBER_OF_WORDS) or (len(all_lines) <
                                                    NUMBER_OF_WORDS):
            self.complete = False
        else:
            self.complete = True
            for line in all_lines:
                split_line = line.split("-")
                word = split_line[0]
                clue = split_line[1]
                word_clue = WordClue(word, clue)
                self.cluelist.append(word_clue)
                word_object = WordUtilities()
                self.word_slices += (word_object.slicer(word))

    def get_slices(self):
        """Return the slices of the words.

        Returns:
            list: List of WordSlice objects.

        """
        return self.word_slices

    def get_word_clues(self):
        """Return the clues of the words.

        Returns:
            list: List of WordClue objects.

        """
        return self.cluelist

    def __str__(self):
        """Return formatted information of words, clues, and slices.

        Returns:
            str: A list of clues and the words' slices.

        """
        string = "Cluelist\n"
        all_lines = FileUtilities.read_lines_from_file(self.filename,
                                                       7)
        for line in all_lines:
            string += f'{line}\n'

        string += "\nSlices\n"
        for sliced in self.word_slices:
            sliced = str(sliced)
            string += f'{sliced}\n'
        return string

    def is_complete(self):
        """Return the status of reading the given file.

        Returns:
            bool: Whether the file has been properly read or not.

        """
        return self.complete
