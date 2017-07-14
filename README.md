# Crowd Finance Infographic

## Assessment

A user wants to produce an infographic that summaries the state of the crowdfunding market over time for use in marketing material and news feeds. Two types of analysis have been proposed:

a) Trending market segments: a ranking of the top trending segments within crowd finance at the end of a given time period, with an indication of where each segment was ranked at the end of an immediately preceding period of time of the same length.
b) Market index: a metric that reflects how well the crowd finance market as a whole performs over a given time period.

Projects adhere to the following schema:

{
	"url": "Link to the campaign on the platform website",
	"platform_name": "Name of Platform",
	"status": "Campaign status",
	"concepts": {
	   "title": ["The concepts within the title"],
	   "subtitle": ["The concepts within the sub title"],
	   "description": ["The concepts within the description"],
	   "category": ["The concepts within the category"]
	 },
	 "start_time": "Project start date.",
	 "end_time": "Project end date. ",
	 "goal_fx": {
		"GBP": "Amount of money campaigning for, in GBP"
	 },
	 "raised_fx": {
		"GBP": "Amount of money currently raised, in GBP"
	 }
}

Where concepts are defined as a list of the following structures:

{
   "start": "The position of the last character of what the concept represents in the corresponding text field (starts at 0)",
   "end": "The position of the last character of what the concept represents in the corresponding text field (starts at 0)",
   "concept": "The actual concept"
}

## Task

Please submit a Python program I can use to generate the analytics results described in a), over an arbitrary time period.

One way of ranking market segments is by the number of times the concepts occur in campaigns. Consider the limitations of this approaches and please improve on it with your solution so it is more informative. __Hint__: Does the popularity of a concept over previous months define whether it is trending this month?

You should output the results in a format that makes it easy to render as a chart (e.g as a JSON document). You should create at least one unit test to verify your code.

### Bonus question
One way to implement the market index would be to compute the total amount raised by all campaigns that end before the specified date. Discuss the limitations and any improvements on this approach that you can think of.

## Instructions

Please submit:

- Your solution for each part of the question.
- Your reasons behind any design decision.
- The limitations of your solution.
- How you could extend your work.
- Instructions on how to use your solutions.

Don't forget to include the requirements.txt file if you've used any external libraries.
