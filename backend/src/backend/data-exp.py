# Gonna try and do some simple data analysis on the data we have

import requests
import datetime
from dateutil import parser


def get_generation_data(start_date: datetime):
    '''From the national grid, get the generation data for a 24 hour period'''
    url = f"https://api.carbonintensity.org.uk/generation/{start_date}/pt24h"
    response = requests.get(url)
    return response.json()


def print_data_for_date(start_date: datetime):
    '''Generate data for a given data in an easy to read format
    :param start_date: The start date of the data
    :return: None
    Will print the data in the following format:
    coal:
    gas:
    solar:
    hydro:
    wind:
    biomass:
    nuclear:
    imports:
    other:
    '''
    # {"data":[{"from":"2023-01-14T11:30Z","to":"2023-01-14T12:00Z","generationmix":[{"fuel":"biomass","perc":1.5},{"fuel":"coal","perc":0.7},{"fuel":"imports","perc":15.1},{"fuel":"gas","perc":7.3},{"fuel":"nuclear","perc":14.8},{"fuel":"other","perc":0},{"fuel":"hydro","perc":2.1},{"fuel":"solar","perc":3.6},{"fuel":"wind","perc":54.9}]},{"from":"2023-01-14T12:00Z","to":"2023-01-14T12:30Z","generationmix":[{"fuel":"biomass","perc":1.7},{"fuel":"coal","perc":0.6},{"fuel":"imports","perc":15},{"fuel":"gas","perc":7.1},{"fuel":"nuclear","perc":14.7},{"fuel":"other","perc":0},{"fuel":"hydro","perc":1.9},{"fuel":"solar","perc":4},{"fuel":"wind","perc":55.1}]},{"from":"2023-01-14T12:30Z","to":"2023-01-14T13:00Z","generationmix":[{"fuel":"biomass","perc":1.6},{"fuel":"coal","perc":0.4},{"fuel":"imports","perc":15.1},{"fuel":"gas","perc":7},{"fuel":"nuclear","perc":14.5},{"fuel":"other","perc":0},{"fuel":"hydro","perc":1.8},{"fuel":"solar","perc":4.1},{"fuel":"wind","perc":55.4}]}
    data = get_generation_data(start_date.isoformat())
    for item in data['data']:
        print(f"\nDate: {parser.parse(item['from'])}")
        # Print the generation mix in descending order
        for fuel in sorted(item['generationmix'], key=lambda x: x['perc'], reverse=True):
            print(f"{fuel['fuel']}: {fuel['perc']}%")


def main():
    print_data_for_date(datetime.datetime(2020, 1, 1))


if __name__ == '__main__':
    main()
