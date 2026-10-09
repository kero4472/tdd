import os
import sys
import unittest
import fire_gdp 


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        header = ['Area', 'Year', 'Forest fires']

        result = fire_gdp.get_column_index(header, 'Year')

        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
