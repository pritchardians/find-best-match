# find_best_match

<!-- TOC -->

* [find_best_match](#find_best_match)
    * [Summary](#summary)
    * [Problem Statement](#problem-statement)
    * [Initial Setup](#initial-setup)
    * [Note on Naming](#note-on-naming)
    * [Early Design Decisions](#early-design-decisions)
    * [Sample JSON](#sample-json)

<!-- TOC -->

## Summary

An open source Python project to consume a set of candidates (each consisting of a list of attributes with an associated
score for each attribute) and match them against a comparator (a list of attributes with an associated weight).
Return a list of the best match(es), as defined by the lowest difference score (a sum of the difference scores of all
the attributes). Examples below may clarify this!<br><br>
**Collaborators should be aware, and follow this [Team Agreement](_TeamAgreement.md).**

## Problem Statement

There are many use cases to take a set of candidates with attributes and scores and match them against a set of
attributes and weights to see which is the best match.
For instance, candidates for a job, matches on a dating site etc. <br><br>

But the algorithms are often hidden, proprietary and may contain bias. <br><br>

This tool is open sourced and the algorythm is exposed through code, documentation etc. So consumers can see how the
matching decision is made. <br><br>

## Initial Setup

- Create virtual environment ```python -m venv venv``` <-- **_NOTE_**: The second _venv_ ref is the directory for the
  virtual environment. Feel free to choose your own directory name, and change the next instruction to match!
- activate virtual environment ```. venv/Scripts/activate```
- Install pip packages ```pip install -r requirements.txt```

## Note on Naming

Naming is hard :) Naming the list of candidates was easy (candidates) but naming the set of attributes, scores and
weights that we are matching against was strangely difficult. I landed on the imperfect *comparator*. Let's just say
that is the term I'm least unhappy with! <br><br>
If any contributors can think of a better name please start a discussion. A universal name change will be easy and,
because of the high level of automatic testing, safe.

## Early Design Decisions

- The request will always receive a response rather than a failure. So if required values
  are not sent in the request, they will be defaulted, a warning emitted and our best result sent back. The warnings
  show
  where issues with the request will affect the matching choice. Here are initial defaults. Each results in a warning
  in the response
    - In the comparator:
        - If an attribute exists more than once, delete all but the first such attribute
        - If no perfect_score exists, or it isn't an integer, default it to 100
        - If no weight exists, or it isn't an integer between 1 and 100, default to 100
    - In the candidates
        - If a candidate exists more than once, delete all but the first such candidate
        - If an attribute does not exist for a candidate, default its value to 0
        - If a candidate has extra attributes, ignore them
- Do NOT choose randomly where more than one candidate has the highest score. Return the full set of top matches,
  and the requester can choose how to treat these results
- Once published as v_1.0.0 and beyond, the API request and response contract should never change - never break code
  that calls it!

## Sample JSON

Readme with notes on JSON samples are [here](sample_json/sample_json_readme.md) <br>
Sample request is here - [request.json](sample_json/request.json) <br>
Sample response is here - [response.json](sample_json/response.json)