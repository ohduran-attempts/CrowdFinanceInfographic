"""Test cases for the project."""
import sys
import unittest

# Import modules from sample
sys.path.insert(0, 'sample')
import core
import helpers

# Set up the data that we are using in tests.
data = helpers.open_json_as_dict('jsons/bigsample.json')


class BasicTest(unittest.TestCase):
    """Basic Test functionality."""

    def test_data_is_not_None(self):
        """Data dictionary brought by the set up is valid."""
        # Test data is displayed as dictionary
        self.assertIsNotNone(data)  # is not None
        self.assertIsInstance(data, list)  # is a list of dictionaries
        for i in range(len(data)):
            self.assertIsInstance(data[i], object)  # entries are dictionaries
            # Test structure of the data
            self.assertIsInstance(data[i]['url'], unicode)
            self.assertIsInstance(data[i]['status'], unicode)
            self.assertIsInstance(data[i]['goal_fx']['GBP'], float)
            self.assertIsInstance(data[i]['start_time'], unicode)
            self.assertIsInstance(data[i]['end_time'], unicode)
            self.assertIsInstance(data[i]['goal_fx'], object)
            # It is either an integer or a float
            self.assertTrue(
                isinstance(data[i]['goal_fx']['GBP'], int) or
                isinstance(data[i]['goal_fx']['GBP'], float))
            self.assertIsInstance(data[i]['raised_fx'], object)
            # It is either an integer or a float
            self.assertTrue(
                isinstance(data[i]['raised_fx']['GBP'], int) or
                isinstance(data[i]['raised_fx']['GBP'], float))

            # Some doesn't include concepts.
            try:
                self.assertIsInstance(data[i]['concepts'], object)
                for j in range(len(data[i]['concepts'])):
                    self.assertIsInstance(
                        data[i]['concepts'][j]['start'], int)
                    self.assertIsInstance(
                        data[i]['concepts'][j]['end'], int)
                    self.assertIsInstance(
                        data[i]['concepts'][j]['concept'], unicode)
            except KeyError:
                pass


if __name__ == '__main__':
    unittest.main()
