import logging
from .piece import Piece
from utils import log_it

log = logging.getLogger(__name__)


class Rook(Piece):
    value = 4
    moves = [[0, 1, 0], [1, 0, 0], [0, 1, 0]]
    attack = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    Special_initial_move = [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
    special_initial_move_length = 2
    has_directionality = True


@log_it
def main():
    pass


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
