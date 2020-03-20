import requests
import json
from termcolor import colored

full_url = f'https://covid2019-api.herokuapp.com/v2/current'
request = requests.get(full_url)
json_ = request.json()

for item in json_['data']:
    print(f"{colored(item['location'], 'yellow')} Confirmed: {colored(item['confirmed'], 'blue')}, Deaths: {colored(item['deaths'], 'red')}, Recovered: {colored(item['recovered'], 'green')}")
