import logging
import os


def configure_logger(filename: str = "app_log.log", level: int = logging.DEBUG) -> None:
    """Configure Logger. Reformat logs to add date and level, and output to a specified path/file

    :param filename: Name of the file to send logs to
    :param level: Logging level using the logging enumerator
    :return: None
    """
    logging.basicConfig(
        filename=filename,
        filemode='w',
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d: %H:%M:%S",
        level=level
    )
    logging.debug("Logs configured by configure_logger function")


if __name__ == "__main__":
    configure_logger()
