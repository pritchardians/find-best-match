import os
import pytest

from src.validate_json import validate_json


# ToDo: Refactor me! This uses 2 similar fixtures and functions.
#  Feed the sample name into 1 function?
# ToDo: Can fixtures have inputs? Or convert to standard functions?

@pytest.fixture
def sample_request():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    sample_request_file = open(f"{this_dir}/request.json")
    return sample_request_file.read()


def read_file(filename: str) -> str:
    """
    Open a file and return its contents as a string. Use a relative filepath
    :param filename: filename to open
    :return: the data in the file
    :rtype: str
    """
    this_dir = os.path.dirname(os.path.realpath(__file__))
    sample_request_file = open(f"{this_dir}/{filename}")
    return sample_request_file.read()


def test_validate_json_request():
    assert validate_json(read_file("request.json")) is True


def test_validate_json_response():
    assert validate_json(read_file("response.json")) is True


if __name__ == '__main__':
    test_validate_json_request()
    test_validate_json_response()
