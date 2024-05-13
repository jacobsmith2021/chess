"""
playable and simulated chess game
5/12/24
TODO
    1) sum player piece value
    2) make simulation
    3) make strategy objects
"""

import logging
from utils import log_it
from board import Board
from termcolor import colored, COLORS

log = logging.getLogger(__name__)


@log_it
def main():
    board = board = Board(x_len=8, y_len=8, num_players=2)
    for player in board.players:
        colors = list(COLORS.keys())
        color = colors[player.get_id() * -1 - 2]
        result = input(colored("please enter piece to move: ", color))
    log.info(f"result is {result}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
