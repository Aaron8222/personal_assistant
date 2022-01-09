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
    tts = gTTS(text,lang='en',tld='co.uk')
    file_name = r'temp\voice.mp3'
    tts.save(file_name)
    playsound(file_name)
    delete_file(file_name)


def speech_to_text(file_name):
    # initialize the recognizer
    r = sr.Recognizer()
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
    delete_file(file_name)
    return text

def listen(file_name, duration):
    # duration in seconds
    fs = 44100  # Sample rate

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int32')
    print('Recording')
    sd.wait()  # Wait until recording is finished
    print('Done')
    write(file_name, fs, myrecording)  # Save as WAV file 

def main():
    while 1:
        file_name = 'temp/output.wav'
        listen(file_name, 2)
        try:
            text = speech_to_text(file_name)
            print(f'What it thinks you said: {text}')
            text_list = text.split()
            #print(text_list)
            guess = {}
            for word in text_list:
                if word.lower() in keywords_dict.keys():
                    if keywords_dict[word] not in guess.keys():
                        guess[keywords_dict[word]] = 1
                    guess[keywords_dict[word]] += 1
            best_guess = sorted(guess, key=guess.get)[-1]
            print(f'It thinks you want: {best_guess}')
            if best_guess == 'joke':
                joke = get_random_joke()
                speak(joke['setup'])
                time.sleep(1)
                speak(joke['punchline'])
            elif best_guess == 'weather':
                data = get_weather()
                weather = data["current"]["weather"][0]['description']
                temperature = data["current"]["temp"]
                weather_report = f"It's currently {weather} and {temperature} degrees celsius"
                speak(weather_report)
        except:
            continue

main()