import os
import vlc
import speak_module 
import random
import subprocess
import datetime

os.system("CLS")

def play_music():
    speak_module.speak("Here you go with music")
    # music_dir = "C:\Users\LUCKY\Music"
    music_dir = "C:\\Users\\Ketan Shah\\Music"
    songs = os.listdir(music_dir)
    num = random.randint(1,len(songs)-1)
    print(songs,len(songs),num)  
    r = os.startfile(os.path.join(music_dir, songs[num]))
    return r

def videos():
    speak_module.speak("Here you go with video")    
    vid_dir = "C:\\Users\\LUCKY\\Videos"
    video = os.listdir(vid_dir)
    num = random.randint(1,len(video)-1)
    print(video,len(video),num)
    r = os.startfile(os.path.join(vid_dir, video[num]))
    return r

def play_focus():
    speak_module.speak("Here you go with video")
    power=r"C:\Users\LUCKY\Videos\Ariana Grande - Focus_HD.mp4"
    os.startfile(power)
    return("playing focus")

def photo():
    speak_module.speak("Here you go with photo")
    photo_dir = "C:\\Users\\Ketan Shah\\OneDrive\\Pictures"
    photos = os.listdir(photo_dir)
    num = random.randint(1,len(photos)-1)
    print(photos,len(photos),num)
    r = os.startfile(os.path.join(photo_dir, photos[num]))
    return r

def power_point():
    speak_module.speak("here you go with power point")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\powerpnt.exe")
    return("opening power point presentation")

def close_powerpoint():
    speak_module.speak("closing power point")
    browserExe = "powerpnt.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed powerpoint")

def word():
    speak_module.speak("here you go with word")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\Winword.exe")
    return ("opening word")

def close_word():
    speak_module.speak("closing word")
    browserExe = "Winword.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed word")

def excel():
    speak_module.speak("here you go with excel")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\excel.exe")
    return ("opening excel")

def close_excel():
    speak_module.speak("closing excel")
    browserExe = "excel.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed excel")

#just creats a file and take notes
def note(usertext):
    date=datetime.datetime.now()
    file_name=str(date).replace(":", "-")+ "-note.txt"
    with open(file_name, "w") as f:
        f.write(usertext)

    p=subprocess.Popen(["notepad.exe",file_name])
    return p

def close_notepad():
    speak_module.speak("closing notepad")
    browserExe = "notepad.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed notepad")

def chrome():
    speak_module.speak("here you go with chrome")
    os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    return ("opening chrome")

def close_chrome():
    speak_module.speak("closing chrome")
    browserExe = "chrome.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed chrome")

def sublime_text():
    speak_module.speak("here you go with sublime text")
    os.startfile(r"C:\Program Files\Sublime Text 3\sublime_text.exe")
    return ("opening sublime text")

def close_sublime_text():
    speak_module.speak("closing sublime text")
    browserExe = "sublime_text.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed sublime text")

def vs_code():
    speak_module.speak("here you go with vs code")
    os.startfile(r"C:\Users\Ketan Shah\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    return ("opening vs code")

def close_vs_code():
    speak_module.speak("closing vs code")
    browserExe = "code.exe" 
    os.system("taskkill /f /im "+browserExe)
    return ("closed vs code")

def shell():
    speak_module.speak("here you go with python shell")
    os.startfile(r"C:\Users\Ketan Shah\AppData\Local\Programs\Python\Python38\Lib\idlelib\idle.pyw")
    return ("opening python shell")