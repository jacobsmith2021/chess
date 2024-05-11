import logging
from .piece import Piece
from utils import log_it

log = logging.getLogger(__name__)


class King(Piece):
    value = None


@log_it
def main():
    pass


if __name__ == "__main__":
    logging.basicConfig()
    log.setLevel(logging.DEBUG)
    main()
