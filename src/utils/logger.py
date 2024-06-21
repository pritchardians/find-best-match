import logging
import os


def configure_logger(filename: str = "app_log.log", level: int = logging.DEBUG) -> None:
    """Configure Logger. Reformat logs to add date and level, and output to a specified path/file
    NOTE: This deletes the app_log.log file in the logs directory to start with a clean log

    :param filename: Name of the file to send logs to
    :param level: Logging level using the logging enumerator
    :return: None
    """
    project_root = "\\".join(os.path.realpath(__file__).split('\\')[:-2]) + "\\logs"
    log_filename = os.path.join(project_root, filename)
    if os.path.exists(log_filename):
        os.remove(log_filename)

    logging.basicConfig(
        filename=log_filename,
        filemode='w',
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d: %H:%M:%S",
        level=level
    )
    logging.debug(f"Logging to: {log_filename}")
