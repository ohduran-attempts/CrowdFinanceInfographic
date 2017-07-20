#!virtualenv/bin/python
from sample import helpers


if __name__ == '__main__':
    filepath = 'jsons/sample.json'
    response, concepts = helpers.get_list_concepts(filepath=filepath)
    print(response)

else:
    print (__name__)
