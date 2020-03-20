"""Gets covid data"""
# External Imports
import requests


def get_data(url):
    """Gets a JSON from a url

    'url' is any full url string
    Returns a dictionary
    """
    request = requests.get(url)
    json_ = request.json()

    return json_['data']
