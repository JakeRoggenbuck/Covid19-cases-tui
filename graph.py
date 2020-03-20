import requests
import numpy as np
import matplotlib.pyplot as plt
from get_covid_data import get_data

json_ = get_data('https://covid2019-api.herokuapp.com/v2/current')

n_groups = len(json_['data'])
location = [item['location'] for item in json_['data']]
confirmed = [item['confirmed'] for item in json_['data']]
deaths = [item['deaths'] for item in json_['data']]
recovered = [item['recovered'] for item in json_['data']]

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, confirmed, bar_width,
alpha=opacity,
color='b',
label='confirmed')

rects3 = plt.bar(index + bar_width, recovered, bar_width,
alpha=opacity,
color='g',
label='recovered')

rects2 = plt.bar(index + bar_width, deaths, bar_width,
alpha=opacity,
color='r',
label='deaths')

plt.xlabel('Location')
plt.ylabel('People')
plt.title('Covid-19 by person')
plt.xticks(index + bar_width, location)
plt.legend()

plt.tight_layout()
plt.show()
