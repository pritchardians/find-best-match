from validate_json import validate_json

# The sample request below is valid, and can be used when calling find_best_match
# NOTE: Shows that a comparator attribute can have a missing perfect_score (defaults to 100)
# NOTE: Shows that a comparator  attribute can have a missing weight (defaults to 100)
# NOTE: Shows that candidates can have missing attributes (default to a score of 0)
# NOTE: Shows that candidates can have extra attributes - they will be ignored
# ToDo: refactor this so the JSON is in a file in a sample json folder, read by the validator, run through auto-tests
validate_json("""
)
