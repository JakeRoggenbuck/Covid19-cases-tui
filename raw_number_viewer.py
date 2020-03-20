"""Grabs Coronavirus data and prints it in color to the terminal"""
# External Imports
from termcolor import colored
# Internal Imports
from get_covid_data import get_data

for item in get_data(f'https://covid2019-api.herokuapp.com/v2/current'):
    print(f"{colored(item['location'], 'yellow')} Confirmed: {colored(item['confirmed'], 'blue')},"
          f" Deaths: {colored(item['deaths'], 'red')}, Recovered: {colored(item['recovered'], 'green')}")
