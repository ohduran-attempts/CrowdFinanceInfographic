#!crowdfinance/bin/python
"""This file includes the core of the project."""
import json
import os


def open_json_as_dict(filepath):
    """Open JSON file and turn it into a dictionary object."""
    with open(filepath, 'r') as f:
        return json.loads(f.read())[0]  # decode not valid.


data = open_json_as_dict('projects.json')

triplets = [triplet
            for text in data['concepts']
            for triplet in data['concepts'][text]]


for i in range(len(triplets)):
    try:
        print str(triplets[i]['concept'])
    except UnicodeEncodeError:
        print i
