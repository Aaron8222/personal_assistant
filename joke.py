import requests
import json

def get_random_joke():
    url = r'https://nova-joke-api.netlify.app/.netlify/functions/index/random_joke'
    response = requests.get(url)
    return json.loads(response.text)