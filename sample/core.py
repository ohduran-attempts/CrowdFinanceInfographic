"""This file includes the core of the project."""

import json
import os


def open_json_as_dict(filepath):
    """Open JSON file and turn it into a dictionary object."""
    with open(filepath, 'r') as f:
        return json.loads(f.read())


def extract_concepts(filepath):
    """From the dict, extract the concepts."""
    data = open_json_as_dict(filepath)
    len_data = len(data)
    concepts = []
    for i in xrange(len_data):
        start_time = data[i]["start_time"]
        end_time = data[i]["end_time"]
        try:
            triplets = [triplet
                        for text in data[i]['concepts']
                        for triplet in data[i]['concepts'][text]]

            for j in range(len(triplets)):
                try:
                    concepts.append([str(triplets[j]['concept']),
                                    start_time,
                                    end_time])
                # avoid concepts that can't be converted into string.
                except UnicodeEncodeError:
                    pass
        # if concepts is missing
        except KeyError:
            pass
    return concepts


def countcampaigns(filepath):
    """Count lines in a JSON file."""
    data = open_json_as_dict(filepath)
    return len(data)
