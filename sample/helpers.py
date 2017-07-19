"""This library supports core.py in its implementation."""
import json
from re import findall
import os


def open_json_as_dict(filepath):
    """Open JSON file and turn it into a dictionary object."""
    with open(filepath, 'r') as f:
        return json.loads(f.read())


def get_campaigns_and_concepts(filepath):
    """From the dict, extract the concepts."""
    data = open_json_as_dict(filepath)
    len_data = len(data)
    JSON = {}
    for i in range(len_data):
        try:  # Avoid incorrectly formated data.
            # REGEX the url and capture the name of the campaign
            campaign_name = findall(
                '(?:\/)((\w+-\w+)+\w+)',  # match: /word-word, ...
                data[i]['url'])
            # controlling for no matches
            if len(campaign_name) != 0:
                campaign_name = campaign_name[0][0]
            else:
                campaign_name = findall(
                    '(?:\/)(?!www)(?!projects)((\w+)+)',  # match: /word
                    data[i]['url'])[0][0]
            start_time = data[i]["start_time"]
            end_time = data[i]["end_time"]
            # each data point will have this info:
            dt_point = {
                'name': campaign_name,
                'start date': start_time,
                'end date': end_time,
                'concepts': []
            }
            # we add the skeleton to the dictionary under key i.
            JSON[i] = dt_point
            # concepts are stored in .json in triplets,
            # address that format then capture the concept.
            triplets = [triplet
                        for text in data[i]['concepts']
                        for triplet in data[i]['concepts'][text]]
            len_triplets = len(triplets)  # avoid recalculation in loops.
            # capturing concept and append to concepts list.
            concepts = [triplets[j]['concept']
                        for j in range(len_triplets)]
            # make concepts unique. Cannot use list comprehension
            # as it validates against the pre-loop value of the list.
            concepts_unique = []
            for item in concepts:
                if item not in concepts_unique:
                    concepts_unique.append(item)
            JSON[i]['concepts'] = sorted(concepts_unique)
        # if format of a given entry is not adequate
        except KeyError:
            pass
    return JSON


def get_concept_list(filepath):
    """
    Create a JSON with each available concept.
    Each will have the start date for all the campaigns available.
    """
    data = open_json_as_dict(filepath)
