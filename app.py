import requests
from termcolor import colored

def get_data(url):
    """Gets a JSON from a url

    'url' is any full url string
    Returns a dictionary
    """
    request = requests.get(url)
    json_ = request.json()
    
    return json_['data']


for item in get_data(f'https://covid2019-api.herokuapp.com/v2/current'):
    print(f"{colored(item['location'], 'yellow')} Confirmed: {colored(item['confirmed'], 'blue')}, Deaths: {colored(item['deaths'], 'red')}, Recovered: {colored(item['recovered'], 'green')}")