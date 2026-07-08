"""
City Functions
CSD-325 Module 7 Assignment
Author: Tj Martin
"""

def city_country(city, country, population=None, language=None):
    """Return a formatted city, country, population, and language string."""
    if population is not None and language is not None:
        return f"{city}, {country} - population {population}, {language}"

    if population is not None:
        return f"{city}, {country} - population {population}"

    return f"{city}, {country}"


# Function calls
    if __name__ == "__main__":

        print(city_country("Santiago", "Chile"))

        print(city_country(
            "Paris",
            "France",
            2100000
        ))

        print(city_country(
            "Madrid",
            "Spain",
            3300000,
            "Spanish"
        ))