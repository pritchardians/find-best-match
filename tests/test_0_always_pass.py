import pytest

from src import test_support


@pytest.mark.parametrize("num_01, num_02, expect", [
    (10, 10, 20),
    (50, -100, -50)
])
def test_app(num_01, num_02, expect):
    assert test_support.count(num_01, num_02) == expect
