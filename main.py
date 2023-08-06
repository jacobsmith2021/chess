import logging
from abc import ABC, abstractmethod

log = logging.getLogger(__name__)


class Board:
    def __init__(self, x_len: int, y_len: int, z_len: int = None):
        if z_len is not None:
            raise NotImplementedError()
        self._board = [[BlankSpace() for _ in range(x_len)] for _ in range(y_len)]
        self._board[0] = self._get_main_row(swap_king=False)
        self._board[1] = self._get_pawn_row(1)
        self._board[-2] = self._get_pawn_row(-2)
        self._board[-1] = self._get_main_row(swap_king=True)
        log.info(f"made board\n{self}")

    def _get_pawn_row(self, row_index: int):
        pawn_row = [Pawn() for _ in range(len(self._board[row_index]))]
        return pawn_row

    @staticmethod
    def _get_main_row(swap_king:bool):
        main_row = [Rook(), Knight(), Bishop(), King(), Queen(), Bishop(), Knight(), Rook()]
        if swap_king:
            temp=main_row[3]
            main_row[3]=main_row[4]
            main_row[4]=temp
        return main_row

    def __repr__(self):
        printable_board = ""
        printable_board += self._print_top()
        printable_board += "\n"
        for row_index in range(len(self._board)):
            printable_board += "|"
            for column_index in range(len(self._board[row_index])):
                element = self._board[row_index][column_index]
                printable_board += str(element)
            printable_board += "|"
            printable_board += "\n"
        printable_board += self._print_top()
        return printable_board

    def _print_top(self):
        return " " + len(self._board) * "-"


class BlankSpace:
    def __repr__(self):
        return " "


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

    def move(self):
        pass

    def attack(self):
        self.move()

    def __repr__(self):
        return str(self.__class__).split(".")[-1][0]


class Pawn(Piece):
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


class Rook(Piece):
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


class Knight(Piece):
    value = 3

    # avoid overlap with King
    def __repr__(self):
        return "N"


class Bishop(Piece):
    value = 3.15


class Queen(Piece):
    value = 9


class King(Piece):
    value = None


def log_it(func):
    def decorated_func(*args, **kwargs):
        log.info(f"Enter {func.__name__}")
        result = func(*args, **kwargs)
        log.info(f"Leave {func.__name__}")
        return result

    return decorated_func


@log_it
def main():
    board = Board(x_len=8, y_len=8)


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
