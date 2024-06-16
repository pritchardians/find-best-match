from validate_json import validate_json

# The sample request below is valid, and can be used when calling find_best_match
# NOTE: Shows that an attribute can have a missing perfect_score (defaults to 100)
# NOTE: Shows that an attribute can have a missing weight (defaults to 100)
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
    "candidates": {}
    
}
""")
