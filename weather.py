import requests
import json
from credentials.api_keys import OPEN_WEATHER_API_KEY
import geocoder

def get_gps_coords():
    g = geocoder.ip('me')
    return g.latlng

def get_weather():
    gps_coords = get_gps_coords()
    lat = gps_coords[0]
    lng = gps_coords[1]
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lng, OPEN_WEATHER_API_KEY)
    response = requests.get(url)
    return json.loads(response.text)
    #current = data["current"]["temp"]
    #print(current)
