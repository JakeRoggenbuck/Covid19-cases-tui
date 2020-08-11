import requests
from termgraph import termgraph as tg
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt
from get_covid_data import get_data

json_ = get_data('https://covid2019-api.herokuapp.com/v2/current')

n_groups = len(json_)
location = [item['location'] for item in json_]
confirmed = [item['confirmed'] for item in json_]
deaths = [item['deaths'] for item in json_]
recovered = [item['recovered'] for item in json_]
active = [item['active'] for item in json_]


colors = [94, 91, 96]

max_width = confirmed[0]/100

data = []
normal_data = []
for item in json_:
    data.append([item['confirmed'], 0, 0]) # 0 for the other two values since for some reason using this API the active deaths and recovered numbers dont add up to be the same as the confirmed cases. This should not effect the graph
    normal_data.append([item['active']/max_width + 1, item['deaths']/max_width + 1, item['recovered']/max_width + 1])

args = {'filename': 'data/ex4.dat', 'title': '', 'width': 100,
    'format': '{:<5.2f}', 'suffix': '', 'no_labels': False,
    'color': None, 'vertical': False, 'stacked': False,
    'different_scale': False, 'calendar': False,
    'start_dt': None, 'custom_tick': '', 'delim': '',
    'verbose': False, 'version': False}

print("Covid 19 Cases per location\n" + colored('▇', 'blue') + " Active\n" + colored('▇', 'red') + " Deaths\n" + colored('▇', 'green') + " Recovered\n")
tg.stacked_graph(location, data, normal_data, 3, args, colors)