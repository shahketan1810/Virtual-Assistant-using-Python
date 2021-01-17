import pyttsx3
import speech_recognition as sr
import pyaudio  #pip install pipwin
                #pipwin install pyaudio
# import os
# import pyaudio 
# import speech_recognition as sr
from database import speak_is_on
from first_of_VA2 import *
import assistant_details

#choosing voice male [0] or female [1]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak (usertext):
    if speak_is_on():
        engine.say(usertext)
        engine.runAndWait()
    else:
        msg = QMessageBox()
        msg.setWindowTitle(f"{assistant_details.name}")
        msg.setText(f"{usertext}")
        x = msg.exec_()        


def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)

        msg = QMessageBox()
        msg.setWindowTitle(f"{assistant_details.name}")
        msg.setText(f"{assistant_details.name} : Listening.....")
        x = msg.exec_()

        print('Listening.....')
        audio=r.listen(source)
       
    said = ""

    try:
        print("Recognizing")
        said = r.recognize_google(audio)

        msg = QMessageBox()
        msg.setWindowTitle("USER")
        msg.setText(f" USER : {said}")
        x = msg.exec_()  # this will show our messagebox

        print('USER: '+said)
    #except Exception as e:
        #   print("Exception:(didn't get that) "+ str(e))
    except sr.UnknownValueError:
        print ('Google Speech Recognition could not understand')
        return ('Google Speech Recognition could not understand')
    except sr.RequestError :
        print('Request error from Google Speech Recognition try checking your internet connection')

    return said.lower()