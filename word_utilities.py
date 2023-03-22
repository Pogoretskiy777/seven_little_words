"""Return list of word splices.

Author: Joseph Pogoretskiy
Version: 12/5/2022
Honor Code: All work is my own.
"""


from word_slice import WordSlice


class WordUtilities():
    """Word slice class.

    Attributes:
        word (str): Inputted word to slice.

    """

    def slicer(self, word):
        """Slices given word correctly based on Seven Little Words rules.

        Args:
            word (str): Word to splice.

        Returns:
            list: List of word slices.

        """
        list_of_splices = []
        if (len(word) % 3 == 0):
            i = 0
            while i < len(word):
                splice = word[i:i+3].upper()
                splice_object = WordSlice(splice)
                list_of_splices.append(splice_object)
                i += 3
            return list_of_splices
        elif (len(word) % 2 == 0):
            i = 0
            while i < len(word):
                splice = word[i:i+2].upper()
                splice_object = WordSlice(splice)
                list_of_splices.append(splice_object)
                i += 2
            return list_of_splices
        else:
            first_splice = word[:3].upper()
            first_splice_object = WordSlice(first_splice)
            list_of_splices.append(first_splice_object)
            i = 3
            while i < len(word):
                splice = word[i:i+2].upper()
                splice_object = WordSlice(splice)
                list_of_splices.append(splice_object)
                i += 2
            return list_of_splices
