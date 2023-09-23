# -*- coding: utf-8 -*-
# Погода


import requests
import json


class Weather_:

    def __init__(self):
        print("init")


    city_name = input("Enter city:")
    API_key = '6af77e2869f7fe9c97d32d743ded2eea'
    api_geocoding = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_key}'
    response = requests.get(api_geocoding)
    json_data = json.loads(response.text)


    for data in json_data:
        lat = data['lat']
        lon = data['lon']


    @classmethod
    def weather(self):
        api_url_base = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
        response = requests.get(api_url_base, params={'units': 'metric', 'lang': 'ru'})
        json_data = json.loads(response.text)
        print("conditions:", json_data['weather'][0]['description'])
        print("temp:", json_data['main']['temp'])
        print("temp_min:", json_data['main']['temp_min'])
        print("temp_max:", json_data['main']['temp_max'])
        print("pressure:", json_data['main']['pressure'])
        print("humidity:", json_data['main']['humidity'])
        print("visibility:", json_data['visibility'])
        print("wind speed:", json_data['wind']['speed'])
