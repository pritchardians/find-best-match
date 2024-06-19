# Team Agreement
<!-- TOC -->
* [Team Agreement](#team-agreement)
  * [About This Agreement](#about-this-agreement)
  * [Summary](#summary)
  * [Technical Principles](#technical-principles)
  * [Branching Strategy](#branching-strategy)
<!-- TOC -->

## About This Agreement
This is a working, living document and can (should) change as new collaborators join the project or as we learn more.
New collaborators should agree with these statements in principle and agree to follow the practices, unless they
get agreement from the team to work in some other way

## Summary
- We all like each other, and we are here to help each other!
- Quality is more important than speed. Nobody will be harmed by taking time to get the work right
- We are proud of this work, and will make decisions to keep us being proud
- This is a helpful project and will cause no harm
- Everything must be transparent and open to review from anyone in the world - especially the matching algorythm
- Differences in opinion are encouraged, debate is awesome, rudeness is terrible, 
eventual consistency of ideas is our goal :)

## Technical Principles
- Code should be simple and self-documenting
- While we love to be Pythonic, we won't let that harm readability
- Everything should be peer-reviewed before being merged to the *develop* or *main* branch
- Code should have pytest tests covering all logic branches before we call it done
- Use reStructure docstrings on all functions / methods etc.
- Use type hinting everywhere
- Nothing causes an unexpected / untrapped error. Find exceptions and deal with them gracefully in the code. 
We always send a valid response!
- Be transparent with data manipulation caused by validation
- Error check, validate, take appropriate actions
- Where we can, follow functional programming principles - small, testable features which - 
if possible - are non-mutating
- Follow the PEP principles
- Build an issue in GitHub before you build the code!

## Branching Strategy
**_NOTE_**: The branching strategy on the develop and main branches (need approved pull request) are enforced by GitHub 
actions
- This branching strategy is based on 
[git-flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) (although we don't use 
git-flow extensions). **ToDo**: _Discussion - should we? Would they help?_
- The *main* branch is always a mirror of deployed code. It always works!
- The *develop* branch is where we commit tested changes
- Create feature branches from *develop* and merge them in to *develop* when tested
- Let's avoid merge conflicts through talking to each other!
- Pull code from *develop* often to make sure you are working off the most recent working code
