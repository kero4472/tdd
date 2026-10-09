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


class TestGetData(unittest.TestCase):

    def test_get_all_rows(self):

        file_name = 'test/data/test_co2.csv'

        result = fire_gdp.get_data(file_name)

        expected = [
            ['Brazil', '2000', '150.5'],
            ['Brazil', '2001', '200.2'],
            ['Brazil', '2002', ''],
            ['Canada', '2000', '75.3']
        ]

        self.assertEqual(result, expected)

    def test_filter_country(self):

        file_name = 'test/data/test_co2.csv'

        result = fire_gdp.get_data(
            file_name,
            query_column=0,
            query_value='Brazil'
        )

        expected = [
            ['Brazil', '2000', '150.5'],
            ['Brazil', '2001', '200.2'],
            ['Brazil', '2002', '']
        ]

        self.assertEqual(result, expected)

    def test_return_header(self):

        file_name = 'test/data/test_co2.csv'

        result = fire_gdp.get_data(
            file_name,
            return_header=True
        )

        expected_header = ['Area', 'Year', 'Forest fires']

        expected_rows = [
            ['Brazil', '2000', '150.5'],
            ['Brazil', '2001', '200.2'],
            ['Brazil', '2002', ''],
            ['Canada', '2000', '75.3']
        ]

        self.assertEqual(result, (expected_header, expected_rows))

    def test_filter_country_with_header(self):

        file_name = 'test/data/test_co2.csv'

        result = fire_gdp.get_data(
            file_name,
            query_column=0,
            query_value='Brazil',
            return_header=True
        )

        expected_header = ['Area', 'Year', 'Forest fires']

        expected_rows = [
            ['Brazil', '2000', '150.5'],
            ['Brazil', '2001', '200.2'],
            ['Brazil', '2002', '']
        ]

        self.assertEqual(result, (expected_header, expected_rows))


class TestGetFireGdpYearData(unittest.TestCase):

    def test_brazil_2000(self):

        co2_file = 'test/data/test_co2.csv'
        gdp_file = 'test/data/test_gdp.csv'
        country = 'Brazil'

        result = fire_gdp.get_fire_gdp_year_data(co2_file, gdp_file, country)

        expected = [
            [2000, 150.5, 1000.0],
            [2001, 200.2, 1200.0],
        ]

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
