import logging
from .piece import Piece
from utils import log_it

log = logging.getLogger(__name__)


class Pawn(Piece):
    value = 1
    move_length = 1
    can_promote = True
    special_initial_move = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    special_initial_move_length = 2
    moves = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]

    attacks = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]


@log_it
def main():
    pass


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
