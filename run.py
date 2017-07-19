#!crowdfinance/bin/python
from sample import core


if __name__ == '__main__':
    filepath = 'bigsample.json'
    response = core.get_concept_dates(filepath)
    print response
else:
    print __name__
