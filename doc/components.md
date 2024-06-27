# Components

### API: Provision for users to provide the necessary input
The API component will be responsible for providing a means for the user to provide information about the candidates and the archetype against which they will be compared.

The request payload must contain one or more candidates in a list, each candidate composed of a list of attributes and their ratings. 

The architype will consist of a list of attributes, their ideal ratings and a weight for calculation. 
The API will return a response payload in real time. The results will consist of information about the ideal candidate based on the calculations, as well as any warnings regarding default values being used or invalid data being disregarded, for the candidate or the archetype. 

### Rules Engine: Translate the ideal ratings and weights into a tool to perform the calculation
The Rules Engine is responsible for reading the Archetype information from the request payload and converting that into rules that will be used to make the comparisons, as well as providing functions to pass in a candidate and get a rating for that candidate based on the rules.

The Rules Engine will be repsonsible for applying a set of criteria for processing the attributes of the archetype. Any attribute that lacks an ideal rating will have an assumed ideal rating of 100, and any attribute missing a weight will have an assumed weight of 100. If an attribute appears more than once, only the first isntance will be accepted, any others discarded.

### Comparison Engine: Process a list of candidates
The Comparison Engine takes in the list of candidates, processes them, submits them to the Rules Engine and ranks them.

If a candidate of the same name appears twice in the same list, only the first one encountered in the list will be valid and included in the ranking process. Any attributes that are missing will be assumed to have a value of 0. Any attributes associated with the candidate that are not present in the archetype (detailed below) will be disregarded. If an individual has more than one instance of the same attribute, only the first one encountered will be accepted, any others discarded.

If more than one candidate has the same rank, all such candidates will be provided to the API to be returned to the caller.

### Warning Checker: Read the input and maintain a list of warnings based on missing data
The Warning Checker serves as a logging tool for any modifications made to the archetype by the Rules Engine or the candidates by teh Comparison Engine.

For every attribute in the ideal, make note of any defaults applied or duplicates discarded. For every candidates, make note of any defaults applied or duplicates discarded. 

It will finally provide a method to expose the list of warnings for the response