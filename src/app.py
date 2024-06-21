import logging

from src.utils.logger import configure_logger

if __name__ == '__main__':
    configure_logger()
    logger = logging.getLogger(__name__)
    logger.debug("Main App started")
