"""Testing word utilites.

Author: Joseph Pogoretskiy
Version: 12/5/2022
Honor Code: All work is my own.
"""


import unittest
from word_utilities import WordUtilities


class TestWordUtilities(unittest.TestCase):

    def test_three_divisible(self):
        """Testing cases when words by 3 are correctly spliced and returned."""
        word = WordUtilities()
        literal = word.slicer('imaginary')
        for i in range(len(literal)):
            literal[i] = str(literal[i])
        self.assertEqual(["IMA", "GIN", "ARY"], literal)
        
        literal = word.slicer('hUnGry')
        for i in range(len(literal)):
            literal[i] = str(literal[i])
        self.assertEqual(["HUN", "GRY"], literal)

    def test_two_divisible(self):
        """Testing cases when words evenly divisible by 2 are correctly spliced
        and returned.

        """
        word = WordUtilities()
        literal = word.slicer('examples')
        for i in range(len(literal)):
            literal[i] = str(literal[i])
        self.assertEqual(["EX", "AM", "PL", "ES"], literal)

    def test_non_divisibles(self):
        """Testing cases when words neither divisble by 3 or 2 are correctly
        spliced and returned.

        """
        word = WordUtilities()
        literal = word.slicer('Madison')
        for i in range(len(literal)):
            literal[i] = str(literal[i])
        self.assertEqual(["MAD", "IS", "ON"], literal)

        literal = word.slicer("Mitochondrias")
        for i in range(len(literal)):
            literal[i] = str(literal[i])
        self.assertEqual(["MIT", "OC", "HO", "ND", "RI", "AS"], literal)


if __name__ == "__main__":
    unittest.main()
