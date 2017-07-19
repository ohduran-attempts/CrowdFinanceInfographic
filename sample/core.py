"""This file includes the core of the project."""
from helpers import get_concept_list


def get_concept_dates(filepath):
    """
    Create a JSON with each available concept.
    Each will have the start date for all the campaigns available.
    """
    data = get_concept_list(filepath=filepath)
    return data
 
