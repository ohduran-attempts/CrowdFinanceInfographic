#!crowdfinance/bin/python
from sample import core


if __name__ == '__main__':
    filepath = 'bigsample.json'
    response = core.extract_concepts(filepath)
    print response
else:
    print __name__
