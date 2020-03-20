"""Takes 5 countries from the user and graphs coronavirus data"""
# External Imports
import pygal
# Internal Imports
from get_covid_data import get_data

def take_user_data():
    """Takes the countries the user wants to graph"""
    user_input = input('Enter some countries separated by commas (Case Sensitive): ')
    user_input = user_input.split(',')
    return user_input


def generate_graphs():
    """Generates the graphs based on the countries from the user input"""
    # Grabs json data and User input
    json_data = get_data('https://covid2019-api.herokuapp.com/v2/current')
    # Generates list of all countries based on json data
    countries = [country['location'] for country in json_data]
    user_countries = take_user_data()
    # Iterates through user countries and raises an error if the user country does not exist
    for country in user_countries:
        if country not in countries:
            raise ValueError('Invalid country')
    # Generates a pygal bar graph object
    covid_graph = pygal.Bar()
    # Sets the x labels of the bar graph to this list
    covid_graph.x_labels = ['Confirmed Cases', 'Deaths', 'Recovered']
    # Iterates through the user_countries and adds country data to the bar graph
    for country in json_data:
        if country['location'] in user_countries:
            covid_graph.add(country['location'], [country['confirmed'],
                                                  country['deaths'],
                                                  country['recovered']])
    covid_graph.render_to_file('covid_graph.svg')


generate_graphs()
