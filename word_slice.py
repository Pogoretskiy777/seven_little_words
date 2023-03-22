"""Word slice properties.

Author: Joseph Pogoretskiy
Version: 12/5/2022
Honor Code: All work is my own.
"""


class WordSlice():
    """Word slice class.

    Attributes:
        text (str): word slice
        used (bool): if the word slice is used or not

    """

    def __init__(self, text):
        """Initialize a word and if it is used.

        Args:
            text (str): Word slice.

        """
        self.text = text
        self.used = False

    def is_used(self):
        """Determine if a word slice is used.

        Returns:
            bool: If a word slice is used or not.

        """
        if self.used:
            return True
        else:
            return False

    def reset(self):
        """Reset word slice used property to False."""
        self.used = False

    def use(self):
        """Use word slice."""
        self.used = True

    def __str__(self):
        """Return string based on its used property.

        Returns:
            str: Word slice disappears if used and vice versa.
        """
        if self.used:
            return ""
        else:
            return self.text
