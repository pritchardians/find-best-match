import json


def validate_json(sample_json_to_validate: str) -> bool:
    """
    Validate a sample JSON to uncover syntactic issues
    :param sample_json_to_validate: JSON code we want to validate
    :return: Was the parsing successful?
    :rtype: bool
    """
    try:
        json_deserialized = json.loads(sample_json_to_validate)
    except json.JSONDecodeError as e:
        print("****************\n* INVALID JSON *\n****************\n")
        print(e)
        return False
    print("---------\nValid JSON\n---------\n")
    print(json_deserialized)
    return True


sample_json_to_validate = """
{   "me": "you",
    "more": 25,
    "nested":{"one":1, "two":2}
}
"""

if __name__ == "__main__":
    print(validate_json(sample_json_to_validate))
