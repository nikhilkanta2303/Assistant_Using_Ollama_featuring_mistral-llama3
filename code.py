import ollama
import pyttsx3

engine = pyttsx3.init()  # Initialize the text-to-speech engine
voices = engine.getProperty('voices')  # Get all available voices
engine.setProperty('voice', voices[0].id)  # Set the second voice (index starts from 0)
engine.setProperty('rate', 170)  # Set speaking rate (default is 200)
engine.setProperty('volume', 0.7)  # Set volume from 0 (silent) to 1 (maximum)
#=============================

def ask(pmt):

    response = ollama.chat(model='mistral', messages=[
    {
        'role': 'user',
        'content': pmt+"(summarize in a sentence with 30 words maximum)",
    },
    ])
    res = response['message']['content']
    #print(res)

    #===========================
    print(res)
    engine.say(res)
    engine.runAndWait()  # Wait until the speech is finished

    