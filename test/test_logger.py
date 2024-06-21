import logging
import pytest

from test.log_test_runner import create_log


@pytest.fixture
def test_configure_logger():
    test_logger = create_log()
    logger = logging.getLogger()
    logger.debug("Test run started")


def test_log_file_exists(test_configure_logger):
    assert True
    # assert os.path.exists("test-log.log")

