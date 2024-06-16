from validate_json import validate_json

# This ensures the sample request below is valid, and can be used when calling find_best_match
validate_json("""
{
    "comparator": {
        "attributes": {
        "height": {
                "perfect_score": 25,
                "weight": 100            
            }
    },
    "candidates": {}
    
}
""")
