"""Seven Little Words main modules.

This program starts the seven little words game with a given text file of the
words and clues.

Author: Joseph Pogoretskiy
Version: 12/9/2022
Honor Code: All work is my own.
"""


from game_board import GameBoard
from game_info import GameInfo
import sys


def play_game():
    """Play Seven Little Words."""
    if len(sys.argv) <= 1:
        print("Usage: python seven_little_words.py <game_file>")
    else:
        game = GameInfo(sys.argv[1])
        if not game.is_complete():
            print("Game file is incomplete")
        else:
            board = GameBoard(game)
            board.set_visible(True)


play_game()
