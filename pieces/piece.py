import logging
from abc import ABC, abstractmethod

log = logging.getLogger(__name__)


class Piece(ABC):

    def __init__(self, player_id: int):
        self._player_id = player_id

    @property
    @abstractmethod
    def value(self):
        return None

    @property
    def player_id(self):
        return self._player_id

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


def log_it(func):
    def decorated_func(*args, **kwargs):
        log.info(f"Enter {func.__name__}")
        result = func(*args, **kwargs)
        log.info(f"Leave {func.__name__}")
        return result

    return decorated_func
