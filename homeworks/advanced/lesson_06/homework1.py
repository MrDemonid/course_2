import logging

FORMAT = '{levelname:<8} [{asctime}] {name}.{funcName}(): {msg}'


def create_logger(fn='stderr.txt', lev=logging.INFO):
    logging.basicConfig(filename=fn, format=FORMAT, style='{', level=lev, datefmt='%H:%M:%S')
    log = logging.getLogger(__name__)
    return log


def foo():
    logger.info(f"foo")
    logger.error(f"error: code = {5}")


if __name__ == '__main__':
    logger = create_logger()

    foo()
