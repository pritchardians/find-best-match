# High Level Design
## Components
API: Provision for users to provide the necessary input
- A list of candidates that each contain a list of attributes and their ratings
- A list of attributes with their ideal rating and a weight for calculation
- Return the ideal candidate and any warnings that apply to the ideal model and the ideal candidate

Rules Engine: Translate the ideal ratings and weights into a tool to perform the calculation
- Read in the attributes, ratings and weights
- Adjust for missing or invalid values based on system-wide rules
- Provide a method to return a rating for a candidate based on their attribute ratings

Comparison Engine: Process a list of candidates
- Read the list of candidates, their attributes and ratings
- Adjust for missing or invalid values based on system-wide rules
- Apply each candidate's values to the Rules Engine
- Keep a ranking of candidates
- Return the candidate closest to the ideal (or more than one in case of ties)

Warning Checker: Read the input and maintain a list of warnings based on missing data
- For every attribute in the ideal, make note of any defaults applied or duplicates discarded
- For every candidates, make note of any defaults applied or duplicates discarded
- Provide a method to expose the list of warnings for the response