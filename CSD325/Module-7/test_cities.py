"""
Tests for city_functions.py
CSD-325 Module 7 Assignment
Author: Tj Martin
"""

import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for city_country function."""

    def test_city_country(self):
        """Test that city and country are formatted correctly."""
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

    def test_city_country_population(self):
        """Test that city, country, and population are formatted correctly."""
        formatted_city = city_country("Santiago", "Chile", 5000000)
        self.assertEqual(formatted_city, "Santiago, Chile - population 5000000")

    def test_city_country_population_language(self):
        """Test that city, country, population, and language are formatted correctly."""
        formatted_city = city_country("Madrid", "Spain", 3300000, "Spanish")
        self.assertEqual(formatted_city, "Madrid, Spain - population 3300000, Spanish")

if __name__ == "__main__":
    unittest.main()