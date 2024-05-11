import logging
from .piece import Piece
from utils import log_it

log = logging.getLogger(__name__)


class Knight(Piece):
    value = 3

    # avoid overlap with King
    def __repr__(self):
        return "N"


@log_it
def main():
    pass


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
