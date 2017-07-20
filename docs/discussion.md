## Project discussion

### Code:

- The structure of the JSON provided was not seamless for data analysis. The [helpers.py](sample/helpers.py) module address this difficulty by importing it as a Python-readable dictionary with a more adequate format.
- The code has been written with a goal in mind: keep the abstractions as strong as possible. That, plainly speaking, means that helpers.py will always treat with JSON files and return dictionaries. Thus, when importing helpers module, core module talks only in terms of Python dictionaries, and never in terms of JSON.

### Data:
#### Quality of the data
- The most obvious fact about the json file is that it is huge. So huge it is impractical for experimenting on it, testing assumptions and build code on top of it. Thus, it will be necessary to take subsets of its data: one called [sample.json](jsons/sample.json) that includes the first campaign segment, and accounts for the Minimum Data Representation (MDR), or simply put, the "building bloc sample" of the dataset. Also, [bigsample.json](jsons/bigsample.json) will act as a "gatekeeper" for the code validation: a subset, mid-sized representation of the overall dataset, which will be used for validation of the hypothesis. It consist of the first ~10.000 lines of projects.json, so it is big enough for validating different campaigns and small enough for us to test the waters.
- The structure of the data is inconsistent: most doesn't have "platform_name". For consistency, we extracted the name from the url using Regular Expressions.
- Time intervals, not time points: hard to discuss trending on data intervals instead of data points.
- Attach dates to certain concepts isn't enough: concepts tend to repeat themselves throughout the same campaign. We filter that by only adding a new data point for each campaign.
#### Analysis of the data
Interestingly enough, the assessment suggests counting the number of times a concept happens on a given time, regardless of whether the occurrences were at the same campaign or across different campaigns. Although it would account for a more granularity in terms of how many times someone, somewhere, used that word on a campaign, is oblivious to the fact that, if a given campaign approaches the description of the product by repeating over an over the same term, that doesn't mean that the term is any more trending than others.

That is, if I created a campaign in which I constantly go over the fact that I want to open my own coffee shop, and go over different varieties of coffee into too much detail, that won't make it any more trending than someone that decided to call their campaign "Zuckerberg 2020" and never mention the name of the candidate anymore on the description.

Thus, when counting the occurrences of a given concept, we weren't oblivious to this issue and decided to count each concept just once. If we were to discuss how much frequent a word is correlated with the success or failure of a given campaign, that would be a different issue that I believe is out of the scope of this assessment. In any case, the occurrences have been reported within the campaign anyway (after all, it is information provided, thus increasing reusability of this project).
