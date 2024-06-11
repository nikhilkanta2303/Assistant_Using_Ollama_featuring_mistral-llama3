from code import ask
import speech_recognition as sr
import time
#===========================================
import pyttsx3

engine = pyttsx3.init()  # Initialize the text-to-speech engine
voices = engine.getProperty('voices')  # Get all available voices
engine.setProperty('voice', voices[0].id)  # Set the second voice (index starts from 0)
engine.setProperty('rate', 170)  # Set speaking rate (default is 200)
engine.setProperty('volume', 0.7)  # Set volume from 0 (silent) to 1 (maximum)
#===========================================

def phoenixask():
    engine.say('Yes Boss!')
    engine.runAndWait()
    r = sr.Recognizer()  # Create a recognizer object
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)  # Record audio from the microphone

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except UnboundLocalError as ULE:
        pass

    #pmt = text
    ask(text)
#phoenixask()
def interrupt():
    engine.stop()