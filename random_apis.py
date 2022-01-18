import requests
import json

def get_random_joke():
    url = r'https://nova-joke-api.netlify.app/.netlify/functions/index/random_joke'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['setup'], data['punchline']

def get_random_advice():
    url = r'https://api.adviceslip.com/advice'
    response = requests.get(url)
    data = json.loads(response.text)
    return data["slip"]["advice"]

def get_random_insult():
    url = r'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    response = requests.get(url)
    data = json.loads(response.text)
    return data['insult']