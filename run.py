#!virtualenv/bin/python
"""Executable file."""
from sample import helpers


if __name__ == '__main__':
    # filepath = helpers.unzip_projects_json()
    filepath = 'jsons/sample.json'
    dictionary = helpers.open_json_as_dict(filepath)
    # print(helpers.get_list_concepts(file=dictionary))
    # print(helpers.get_campaigns_and_concepts(file=dictionary))
    print(helpers.get_market_index(filepath=filepath))
else:
    raise Exception('INTERNAL PROBLEM')
