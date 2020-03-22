import speech_recognition as sr
from playsound import playsound
import os
from gtts import gTTS


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk("Hello, what's your name?")
        audio = r.listen(source)

    try:
        response = r.recognize_google(audio)
        print(f"Google Speech Recognition thinks you said {response}")
        response = response.split()
        return response[-1]
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))


def talk(text):
    tts = gTTS(text=text, lang="en")
    audio_file = 'test.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)


name = listen()
talk(f"What a nice name {name}, nice to meet you!")
