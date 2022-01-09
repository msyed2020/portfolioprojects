# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 03:47:23 2022

@author: fredb
"""

import requests
from pprint import pprint

API_Key = "4890b53516c797216f10a8c5554920ff"
weather_location = input("Enter a location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
pprint(weather_data)