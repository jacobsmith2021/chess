import logging
import unittest
from board import Board

log = logging.getLogger(__name__)


class TestChess(unittest.TestCase):

    def test_chess(self):
        board = Board(x_len=8,y_len=8)
        correct_board = """ --------
|RNBKQBNR|
|PPPPPPPP|
|        |
|        |
|        |
|        |
|PPPPPPPP|
|RNBQKBNR|
 --------"""
        self.assertEqual(str(board),correct_board)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
