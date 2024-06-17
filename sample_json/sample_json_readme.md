# Sample request json usage notes
The sample request and response 'work' in the find_best_match process, but they are missing information to show how
defaults are used in the api. Obviously, it's best to use a fully correct request - don't rely on defaults
which could be changed for some business reason

- Shows that a comparator attribute can have a missing perfect_score (defaults to 100)
- Shows that a comparator  attribute can have a missing weight (defaults to 100)
- Shows that candidates can have missing attributes (default to a score of 0)
- Shows that candidates can have extra attributes - they will be ignored

[Sample request](request.json)
