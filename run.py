#  #!crowdfinance/bin/python
from sample import core


if __name__ == '__main__':
    filepath = 'jsons/bigsample.json'
    response, concepts = core.get_list_concepts(filepath=filepath)
    print response

else:
    print __name__
