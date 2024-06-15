import pytest

from src.validate_json import validate_json


@pytest.mark.parametrize("json_string, expected", [
    ('{ "me": "you"}', True),
    ("""{ "me": "you", "more": 25, "nested":{"one":1, "two":2}}""", True),
    ('{ "me": "you"},', False),
    ('{ "me": you}', False),
    ('{ me: "you"},', False)
])
def test_validate_json(json_string, expected):
    assert validate_json(json_string) == expected
