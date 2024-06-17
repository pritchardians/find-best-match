from src.validate_json import validate_json

sample_request = open("request.json")


def test_validate_json():
    assert validate_json (sample_request.read()) is True


if __name__ == '__main__':
    test_validate_json()
