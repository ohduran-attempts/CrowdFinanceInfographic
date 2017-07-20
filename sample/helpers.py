"""
This library supports core.py in its implementation.

Helpers.py aims at extract information from the JSON file in different ways,
to be consumed by core.py as dictionaries. Provides a level of abstraction.
"""
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
    dictionary = {}
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
                'start_date': start_time,
                'end_date': end_time,
                'concepts': []
            }
            # we add the skeleton to the dictionary under key i.
            dictionary[i] = dt_point
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
            dictionary[i]['concepts'] = sorted(concepts_unique)
        # if format of a given entry is not adequate
        except KeyError:
            pass
    return dictionary


def get_list_concepts(filepath):
    """
    Create a dictionary of concepts.
    concept {
        occurrence: int,
        campaigns: {
            date: string,
            money_raised: int
        }
    }
    """
    data = open_json_as_dict(filepath)
    len_data = len(data)
    dictionary = {}
    concepts = []
    for i in range(len_data):
        try:
            date = data[i]['start_time']
            raised = data[i]['raised_fx']['GBP']
            for text in ['title', 'subtitle', 'description', 'category']:
                concepts += [concept['concept']
                                         for concept in data[i]['concepts'][text]]

            # Fill dictionary with the information
            for concept in concepts:
                # if the concept is new to the dictionary
                if concept not in dictionary.keys():
                    dictionary[concept] = {
                        'occurrence': 1,
                        'campaigns': [{
                            'raised': raised,
                            'date': date
                        }]
                    }
                else:
                    # append a new occurrence and add up 1 to the counter
                    dictionary[concept]['occurrence'] += 1
                    dictionary[concept]['campaigns'].append(
                        {'raised': raised, 'date': date})
        except KeyError:
            pass
    return dictionary
