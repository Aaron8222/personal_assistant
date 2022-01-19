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
from random_apis import get_random_joke, get_random_advice, get_random_insult

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
            print(f'What it thinks you said: {text} \n')
            return text
    except sr.UnknownValueError:
        print('No clue what you said, listening again... \n')
        return listen()

def guess_user_want(text_list):
    guess = {}
    for word in text_list:
        if word.lower() in keywords_dict.keys():
            if keywords_dict[word] not in guess.keys():
                guess[keywords_dict[word]] = 1
            guess[keywords_dict[word]] += 1
    if len(guess) == 0:
        return None
    return sorted(guess, key=guess.get)[-1]

def main():
    print('Starting...')
    while 1:
        start_list = listen().split()
        count = 0
        for word in start_list:
            if word == 'hey' or word == 'maple' or word == 'a':
                count += 1
        if count == 2:
            speak('Yes?')
            text_list = listen().split()
            #print(text_list)
            best_guess = guess_user_want(text_list)
            print(f'It thinks you want: {best_guess} \n') 
            if best_guess == 'joke':
                setup, punchline = get_random_joke()
                speak(setup)
                time.sleep(0.5)
                speak(punchline)
            elif best_guess == 'weather':
                weather, temperature = get_weather()
                weather_report = f"It's currently {weather} and {round(temperature)} degrees celsius"
                speak(weather_report)
            elif best_guess == 'advice':
                speak(get_random_advice())
            elif best_guess == 'insult':
                speak(get_random_insult())
            else:
                speak("I'm not sure I understand")

main()