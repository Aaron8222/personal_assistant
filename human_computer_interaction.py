import pyttsx3
from decouple import config

# Text to Speech Conversion
def speak(text, engine):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

speak(engine, 'hi')