import os
import pytest

from src.validate_json import validate_json

# ToDo: Refactor me! This uses 2 similar fixtures and functions. Feed the sample name into 1 function?
# ToDo: Can fixtures have inputs? Or convert to standard functions?

@pytest.fixture
def sample_request():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    sample_request_file = open(f"{this_dir}/request.json")
    return sample_request_file.read()


@pytest.fixture
def sample_response():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    sample_request_file = open(f"{this_dir}/response.json")
    return sample_request_file.read()


def test_validate_json_request(sample_request):
    assert validate_json(sample_request) is True


def test_validate_json_response(sample_response):
    assert validate_json(sample_response) is True


if __name__ == '__main__':
    test_validate_json_request()
    test_validate_json_response()
