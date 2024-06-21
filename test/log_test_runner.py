import logging

from src.utils.logger import configure_logger


def create_log():
    configure_logger("test-log.log", logging.DEBUG)


if __name__ == '__main__':
    create_log()
