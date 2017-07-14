"""This file includes the core of the project."""
import json
import os


def open_json_as_dict(filepath):
    """Open JSON file and turn it into a dictionary object."""
    with open(filepath, 'r') as f:
        return json.loads(f.read().decode('utf-8'))[0]  # decode not valid.


data = open_json_as_dict('sample.json')

triplets = [triplet
            for text in data['concepts']
            for triplet in data['concepts'][text]]


for i in range(len(triplets)):
    print triplets[i]['concept']
