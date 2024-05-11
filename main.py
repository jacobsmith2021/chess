import logging
from utils import log_it
from board import Board

log = logging.getLogger(__name__)


@log_it
def main():
    Board(x_len=8, y_len=8)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
