from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from delete_file import delete_file
import time
from keywords import keywords_dict
from random import randint
from weather import get_weather
from joke import get_random_joke

def speak(text):
    tts = gTTS(text,lang='en',tld='com')
    file_name = r'temp\voice.mp3'
    tts.save(file_name)
    playsound(file_name)
    delete_file(file_name)

def listen():
    try:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f'What it thinks you said: {text}')
            return text
    except sr.UnknownValueError:
        print("No clue what you said, listening again... \n")
        listen()

def guess_user_want(text_list):
    guess = {}
    for word in text_list:
        if word.lower() in keywords_dict.keys():
            if keywords_dict[word] not in guess.keys():
                guess[keywords_dict[word]] = 1
            guess[keywords_dict[word]] += 1
    return sorted(guess, key=guess.get)[-1]

def joke_inquiry():
    joke = get_random_joke()
    speak(joke['setup'])
    time.sleep(1)
    speak(joke['punchline'])

def weather_inquiry():
    data = get_weather()
    weather = data["current"]["weather"][0]['description']
    temperature = data["current"]["temp"]
    weather_report = f"It's currently {weather} and {round(temperature)} degrees celsius"
    speak(weather_report)

def main():
    while 1:
        if listen() == 'hey maple':
            speak('Yes?')
            text_list = listen().split()
            #print(text_list)
            best_guess = guess_user_want(text_list)
            print(f'It thinks you want: {best_guess}')
            if best_guess == 'joke':
                joke_inquiry()
            elif best_guess == 'weather':
                weather_inquiry()

main()