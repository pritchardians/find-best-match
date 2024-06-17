import os
import pytest

from src.validate_json import validate_json


@pytest.fixture
def sample_request():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    sample_request_file = open(f"{this_dir}/request.json")
    return sample_request_file.read()


def test_validate_json(sample_request):
    assert validate_json(sample_request) is True


if __name__ == '__main__':
    test_validate_json()
