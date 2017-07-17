#!crowdfinance/bin/python
from sample import core


if __name__ == '__main__':
    filepath = 'bigsample.json'
    print core.countcampaigns(filepath)
    concepts = core.extract_concepts(filepath)
    print concepts
    print len(concepts)
else:
    print __name__
