from validate_json import validate_json

# The sample request below is valid, and can be used when calling find_best_match
# NOTE: Shows that a comparator attribute can have a missing perfect_score (defaults to 100)
# NOTE: Shows that a comparator  attribute can have a missing weight (defaults to 100)
# NOTE: Shows that candidates can have missing attributes (default to a score of 0)
# NOTE: Shows that candidates can have extra attributes - they will be ignored
# ToDo: refactor this so the JSON is in a file in a sample json folder, read by the validator, run through auto-tests
validate_json("""
{
    "comparator": {
        "attributes": {
            "number_of_pages": {
                "perfect_score": 250,
                "weight": 100            
            },
            "humor_rating": {
                "perfect_score": 57
            },
            "sentence_complexity": {
                "weight": 100 
            },
            "child_friendliness": {
            }
        }
    },
    "candidates": {
        "candidate_01": {
            "attributes": {
                "number_of_pages": 125,
                "humor_rating": 12,
                "child_friendliness": 73
            },
            "candidate_02": {
                "attributes": {
                    "number_of_pages": 47
                }
            },
            "candidate_03": {
                "attributes": {
                    "number_of_pages": 125,
                    "humor_rating": 12,
                    "child_friendliness": 73,
                    "not processed": 23
                }
            }
        }
    }    
}
""")
