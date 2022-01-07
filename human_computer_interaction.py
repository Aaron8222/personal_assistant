from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write

def speak(text):
    tts = gTTS(text,lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound(filename) # prints warning message not sure if becuase laptop is corrupted. Try downgrading playsound?

def speech_to_text(filename):
    # initialize the recognizer
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)
    return text

def listen():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype='int32')
    print('recording')
    sd.wait()  # Wait until recording is finished
    print('done')
    write('temp\output.wav', fs, myrecording)  # Save as WAV file 


listen()
text = speech_to_text('temp\output.wav')
speak(text)