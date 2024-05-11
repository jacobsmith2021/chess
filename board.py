import logging
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King


log = logging.getLogger(__name__)


class Board:
    def __init__(self, x_len: int, y_len: int, z_len: int = None):
        if z_len is not None:
            raise NotImplementedError()
        self._board = [[BlankSpace() for _ in range(x_len)] for _ in range(y_len)]
        if y_len > 1:
            self._board[1] = self._get_pawn_row(1)  # noqa
            self._board[-2] = self._get_pawn_row(-2)  # noqa
        self._board[0] = self._get_main_row(swap_king=False, row_index=0)
        self._board[-1] = self._get_main_row(swap_king=True, row_index=0)
        log.info(f"made board\n{self}")

    def _get_pawn_row(self, row_index: int):
        pawn_row = [Pawn() for _ in range(len(self._board[row_index]))]
        return pawn_row

    def _get_main_row(self, swap_king: bool, row_index: int):
        column_len = len(self._board[row_index])
        main_row = [BlankSpace() for _ in range(column_len)]
        right_index = column_len // 2
        left_index = right_index - 1
        left_side = [Rook(), Knight(), Bishop(), King()]
        right_side = [Rook(), Knight(), Bishop(), Queen()]
        for left_index in range(column_len // 2):
            right_index = column_len - left_index - 1
            if left_index < column_len:
                main_row[left_index] = left_side[left_index]  # noqa
            if right_index < column_len:
                main_row[right_index] = right_side[left_index]  # noqa

        if swap_king:
            temp = main_row[left_index]  # noqa
            main_row[left_index] = main_row[right_index]  # noqa
            main_row[right_index] = temp  # noqa
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


def log_it(func):
    def decorated_func(*args, **kwargs):
        log.info(f"Enter {func.__name__}")
        result = func(*args, **kwargs)
        log.info(f"Leave {func.__name__}")
        return result

    return decorated_func


@log_it
def main():
    log.info(f"main")
    Board(x_len=8, y_len=8)
    log.info(f"end     ")


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
