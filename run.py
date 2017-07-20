#!virtualenv/bin/python
"""Executable file."""
from sample import helpers


if __name__ == '__main__':
    filepath = helpers.unzip_projects_json()
    print(helpers.get_list_concepts(filepath=filepath))
else:
    raise Exception('INTERNAL PROBLEM')
