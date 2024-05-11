import logging

log = logging.getLogger(__name__)


def log_it(func):
    def decorated_func(*args, **kwargs):
        log.info(f"Enter {func.__name__}")
        result = func(*args, **kwargs)
        log.info(f"Leave {func.__name__}")
        return result

    return decorated_func
