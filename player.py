import logging
from utils import log_it
from pieces.piece import Piece
from typing import List
import itertools
from termcolor import colored, COLORS

log = logging.getLogger(__name__)


class Player:
    id_iter = itertools.count()

    def __init__(self):
        self._pieces = []
        self._id = next(self.id_iter)

    def add_piece(self, piece: Piece):
        self._pieces.append(piece)

    def get_piece(self) -> List[Piece]:
        return self._pieces

    def get_id(self) -> int:
        return self._id

    def __repr__(self):
        to_return = f"Player {self._id}"
        for piece in self._pieces:
            colors = list(COLORS.keys())
            index = -1 * self._id - 2
            piece_color = colors[index]
            to_return += f"\n{colored(piece,piece_color)}"
        return to_return


@log_it
def main():
    pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
