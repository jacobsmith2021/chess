import logging
import pprint
from abc import ABC, abstractmethod

log = logging.getLogger(__name__)


class Board:
    def __init__(self, x_len: int, y_len: int, z_len: int = None):
        if z_len is not None:
            raise NotImplementedError()
        self._board = [0 for _ in range(x_len) for _ in range(y_len)]
        log.info(f"made board\n{pprint.pformat(self._board)}")


class Piece(ABC):
    @property
    @abstractmethod
    def value(self):
        return None

    @property
    def maximum_move_length(self):
        return None

    @property
    def can_jump(self):
        return False

    @property
    def can_promote(self):
        return False

    @property
    def special_initial_move(self):
        return None

    @property
    def has_directionality(self):
        return None

    @property
    def moves(self):
        return None

    @property
    def attacks(self):
        return None

    @abstractmethod
    def move(self):
        pass

    def attack(self):
        self.move()


class Pawn:
    value = 1
    move_length = 1
    can_promote = True
    special_initial_move = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    special_initial_move_length = 2
    moves = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    attacks = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


class Rook:
    value = 4
    moves = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 0]]
    attack = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    Special_initial_move = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]
    special_initial_move_length = 2
    has_directionality = True


class Knight:
    value = 3


class Bishop:
    value = 3.15


class Queen:
    value = 9


class King:
    value = None
