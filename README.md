# find_best_match
An open source Python project to consume a set of candidates (each consisting of a list of attributes with an associated
score for each attribute) and match them against a comparator (a list of attributes with an associated weight).
Return a list of the best match(es), as defined by the lowest difference score (a sum of the difference scores of all
the attributes). Examples below may clarify this!

## Problem Statement
There are many use cases to take a set of candidates with attributes and scores and match them against a set of
attributes and weights to see which is the best match.
For instance, candidates for a job, matches on a dating site etc. <br><br>

But the algorithms are often hidden, proprietary and may contain bias. <br><br>

This tool is open sourced and the algorythm is exposed through code, documentation etc. So consumers can see how the
matching decision is made. <br><br>