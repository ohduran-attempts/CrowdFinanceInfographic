#  #!crowdfinance/bin/python
from sample import core


if __name__ == '__main__':
    filepath = 'jsons/bigsample.json'
    response = core.get_list_concepts(filepath=filepath)
    for key in sorted(response.keys()):
        try:
            print key, response.keys().count(key)
        except UnicodeEncodeError:
            pass

else:
    print __name__
