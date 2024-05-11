import logging
from utils import log_it
from .piece import Piece

log = logging.getLogger(__name__)


class Queen(Piece):
    value = 9


@log_it
def main():
    pass


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
