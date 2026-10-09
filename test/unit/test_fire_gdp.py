from email import header
import os
import sys
import unittest
import fire_gdp 


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        header = ['Area', 'Year', 'Forest fires']

        result = fire_gdp.get_column_index(header, 'Year')

        self.assertEqual(result, 1)

    def test_name_missing(self):
        header = ['Area', 'Year', 'Forest fires']

        result = fire_gdp.get_column_index(header, 'GDP')

        self.assertIsNone(result)

    def test_empty_header(self):
        header = []

        result = fire_gdp.get_column_index(header, 'Year')

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
