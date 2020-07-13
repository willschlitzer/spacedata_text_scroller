"""Queries the People in Space API for the current people in space"""

import requests


def astros():
    """Queries the API"""
    api_url = "http://api.open-notify.org/astros.json"
    astros_data = requests.get(api_url).json()
    # Saves and prints the number of people in space
    astros_number = astros_data["number"]
    astrocrafts = astros_data["people"]
    astronauts = []
    # Returns the number of people in space, and the dictionaries for the astronauts and their craft
    for astronaut in astrocrafts:
        astronauts.append(astronaut["name"])
    return astros_number, astronauts


if __name__ == "__main__":
    astros()
