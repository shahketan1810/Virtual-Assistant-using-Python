from database import speak_is_on
import webbrowser
from speak_module import get_audio,speak
from input_module import take_input
from first_of_VA2 import *
import keyboard
import pywhatkit
import os
from datetime import datetime,date
os.system("CLS")

def open_whatsapp(self):
    speak("tell number of reciever")
    if speak_is_on():
        reciver = take_input(self)
    else:
        reciver = take_input(self)    
    speak("say your context")
    if speak_is_on():
        context = take_input(self)
    else:
        context = take_input(self)

    try: 
        now = datetime.now()

        hour = int(now.strftime("%H"))
        minute = int(now.strftime("%M"))
        print(f"Reciver : {reciver}")
        print(f"Context : {context}")
        print(f"{hour}")
        print(f"{minute}")
        # sending message to reciever 
        # using pywhatkit 
        pywhatkit.sendwhatmsg(f"+91{reciver}", f"{context}", hour, minute+1)
        return("Successfully Sent!") 

    except: 
        
        # handling exception 
        # and printing error message 
        return("An Unexpected Error!")


def open_facebook():
    webbrowser.open("https://facebook.com")

def close_facebook():
    webbrowser.close("https://facebook.com")

def open_google():
    webbrowser.open(f"https://google.com")


def open_spotify():
    webbrowser.open("https://spotify.com")


def open_gfg():
    webbrowser.open("https://www.geeksforgeeks.org/")


def open_youtube():
    speak("on it sir! what do you want me to play")
    what=get_audio()
    pywhatkit.playonyt(what)

        
def open_stackof():
    webbrowser.open("https://stackoverflow.com/")


def open_git():
    webbrowser.open("https://github.com/")


def open_wynk():
    webbrowser.open("https://wynk.in/music")

def open_comsites(self):
    speak("say com site name")
    if speak_is_on():
        said1 = take_input(self)
    else:
        said1 = take_input(self)     
    said = said1.lower().replace(" ","")
    webbrowser.open(f"https://{said}.com")
    return (said)

def open_sites(self):
    speak("say site name with its dot extension")
    if speak_is_on():
        said1 = take_input(self)
    else:
        said1 = take_input(self)
    said = said1.lower().replace(" ","")
    webbrowser.open(f"https://{said}")
    return (said)


def search(said1):
    said1=said1.replace('search',"")
    site = said1[0:said1.index(" ")].strip()
    query = said1[said1.index(" ")+1:].strip()    
    webbrowser.open(f"https://www.{site}/search?q={query}")
    return (query)  

def imgsearch(said1):
    said1=said1.replace('show images of',"")
    webbrowser.open(f"https://www.google.co.in/search?q="+said1+"&source=lnms&tbm=isch")
    return (said1)

def play(said1):
    said1=said1.replace('play',"")
    site = said1[0:said1.index(" ")].strip()
    query = said1[said1.index(" ")+1:].strip()  
    try:
        pywhatkit.playonyt(query)
        return (query)
    except :
        return("NETWORK ERROR OCCURED")