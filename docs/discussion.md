## Project discussion

### Code:
- The structure of the JSON provided was not seamless for data analysis. The [helpers.py](sample/helpers.py) module address this difficulty by importing it as a Python-readable dictionary with a more adequate format.
- The code has been written with a goal in mind: keep the abstractions as strong as possible. That, plainly speaking, means that helpers.py will always treat with JSON files and return dictionaries. Thus, when importing helpers module, core module talks only in terms of Python dictionaries, and never in terms of JSON.


### Data:
- time intervals, not time points: hard to discuss trending on data intervals instead of data points.
- attach dates to certain concepts isn't enough: concepts tend to repeat themselves throughout the same campaign.
