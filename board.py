import logging
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from player import Player
from termcolor import colored, COLORS


log = logging.getLogger(__name__)


class Board:
    def __init__(self, x_len: int, y_len: int, z_len: int = None, num_players: int = 2):
        if z_len is not None:
            raise NotImplementedError()
        if num_players != 2:
            raise NotImplementedError()
        self._board = [[BlankSpace() for _ in range(x_len)] for _ in range(y_len)]
        self.players = [Player() for _ in range(num_players)]
        if y_len > 1:
            self._board[1] = self._get_pawn_row(1, player=self.players[0])  # noqa
            self._board[-2] = self._get_pawn_row(-2, player=self.players[-1])  # noqa
        self._board[0] = self._get_main_row(
            swap_king=False, row_index=0, player=self.players[0]
        )
        self._board[-1] = self._get_main_row(
            swap_king=True, row_index=0, player=self.players[-1]
        )
        log.info(f"made board\n{self}")

    def _get_pawn_row(self, row_index: int, player: Player):
        pawn_row = [
            Pawn(player_id=player.get_id()) for _ in range(len(self._board[row_index]))
        ]
        for pawn in pawn_row:
            player.add_piece(pawn)
        return pawn_row

    def _get_main_row(self, swap_king: bool, row_index: int, player: Player):
        column_len = len(self._board[row_index])
        main_row = [BlankSpace() for _ in range(column_len)]
        right_index = column_len // 2
        left_index = right_index - 1
        player_id = player.get_id()
        left_side = [
            Rook(player_id=player_id),
            Knight(player_id=player_id),
            Bishop(player_id=player_id),
            King(player_id=player_id),
        ]
        right_side = [
            Rook(player_id=player_id),
            Knight(player_id=player_id),
            Bishop(player_id=player_id),
            Queen(player_id=player_id),
        ]
        for piece in left_side:
            player.add_piece(piece)
        for piece in right_side:
            player.add_piece(piece)
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
        colors = list(COLORS.keys())
        for row_index in range(len(self._board)):
            printable_board += f"{row_index+1}|"
            for column_index in range(len(self._board[row_index])):
                element = self._board[row_index][column_index]

                index = -1 * element.player_id - 2
                piece_color = colors[index]

                printable_board += colored(element, piece_color)

            printable_board += "|"
            printable_board += "\n"
        printable_board += self._print_top()
        files = [chr(x) for x in range(ord("A"), len(self._board[-1]) + ord("A"))]
        files_row = " "
        for file in files:
            files_row += file
        printable_board += f"\n {files_row}"
        return printable_board

    def _print_top(self):
        return "  " + len(self._board) * "_"


class BlankSpace:
    def __repr__(self):
        return " "

    @property
    def player_id(self):
        return -1


def log_it(func):
    def decorated_func(*args, **kwargs):
        log.info(f"Enter {func.__name__}")
        result = func(*args, **kwargs)
        log.info(f"Leave {func.__name__}")
        return result

    return decorated_func


@log_it
def main():
    Board(x_len=8, y_len=8)


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
