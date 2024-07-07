# This package will offer and object definition for a Rules Engine object
#   that will take in a JSON object that conforms to the definition of the
#   'comparator' portion of the request payload. It will parse that data
#   into a set of rules for processing against future inputs in the form of
#   candidates.
#
# init method should take an optional JSON object as a parameter
# warnings method should return a JSON object containing all warnings
#   generated when the comparator was loaded
# rate method should take a candidate JSON object and return their rating
#   based on the rules in the engine