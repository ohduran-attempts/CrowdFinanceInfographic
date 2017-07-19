"""Test cases for the project."""
import sys
import unittest

# Import modules from sample
sys.path.insert(0, 'sample')
import core
import helpers


data = helpers.open_json_as_dict('jsons/sample.json')

class BasicTest(unittest.TestCase):
    """Basic Test functionality."""

    def test_data_is_not_None(self):
        """Data dictionary brought by the set up is valid."""
        self.assertIsNotNone(data)  # is not None
        self.assertIsInstance(data, object)  # is a dictionary



if __name__ == '__main__':
    unittest.main()
