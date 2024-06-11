import speech_recognition as sr
from main import phoenixask



def my_function():
    print("Pheonix Invoked")
    # Add your specific actions here
    phoenixask()


def listen_for_keyword(keyword):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for keyword...")
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()  # Convert recognized text to lowercase (optional)
            if keyword in text:
                print(f"Keyword '{keyword}' recognized!")
                my_function()
            else:
                print("Keyword not recognized.")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except UnboundLocalError as ULE:
            pass
        #recall need to be done
        listen_for_keyword(keyword)

listen_for_keyword("phoenix")  # Replace "your_keyword" with your desired keyword