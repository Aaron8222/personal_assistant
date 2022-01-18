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


# def speech_to_text(file_name):
#     # initialize the recognizer
#     r = sr.Recognizer()
#     with sr.AudioFile(file_name) as source:
#         # listen for the data (load audio to memory)
#         audio_data = r.record(source)
#         # recognize (convert from speech to text)
#         text = r.recognize_google(audio_data)
#     delete_file(file_name)
#     return text

# def listen(file_name, duration):
#     # duration in seconds
#     fs = 44100 # Sample rate
#     start = time.perf_counter()
#     myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int32')
#     print('Recording')
#     sd.wait()  # Wait until recording is finished
#     print('Done')
#     end = time.perf_counter()
#     print(f'Finished in {round(end-start, 2)} second(s)')
#     write(file_name, fs, myrecording)  # Save as WAV file

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

# def start_inquiry(file_name, phrase):
#     text = speech_to_text(file_name)
#     if text == phrase:
#         return True

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