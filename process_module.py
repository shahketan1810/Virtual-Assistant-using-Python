from output_module import give_output
from time_module import get_time,get_date
from input_module import take_input
from first_of_VA2 import *
import database
import internet
import assistant_details 
from web_jobs import *
import system_task
import assistant_details
import pyjokes
import time
import wolframalpha
client = wolframalpha.Client('56QWJV-AYWH7KWPRT')

def adding_query(self,quest):
    give_output('i dont know this one, can you tell me what it mean keyword add')
    ans = take_input(self)
    if "add" in ans:
        ans = ans.replace("add","")
        ans.strip()

        value = database.get_answers_from_memory(ans)
        if value=="":
            return("can't help with this one")
        else:
            database.insert_question_and_answer(quest,value)
            return "thanks i will remember it for the next time"
    elif "no" == ans:
        return("okay")
    else:
        return ("can't help with this")

def process(self,quest):

    answer = database.get_answers_from_memory(quest)
    
    if answer == "get time details":
        return(f'Time is {get_time()}')

    elif answer == "check internet connection":
        if internet.check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    
    elif answer == 'tell date':
        return ("date is "+get_date())

    elif answer == '100':
        return('I am fine, Thank you How are you, Sir')

    elif answer == '101':
        return("It's good to know that you are fine")

    elif answer == '102':
        return(f"my friend call me {assistant_details.name}")

    elif answer == "103":
        return("i have been created by KP KETAN KISHAN")

    elif answer == "104":
        return (pyjokes.get_joke())

    elif answer == "105":
        return ("if you talk then definately you are human")

    elif answer == "106":
        return("Thanks to KP. Further it is secret")

    elif answer == "107":
        return ("i am you virtual assistant created on 9th september")

    elif answer == "108":
        return ("i was created as a minor project by kumar priyanshu,ketan shah,kishan guta ")

    elif answer == "109":
        return (system_task.power_point())

    elif answer == "close powerpoint":
        return (system_task.close_powerpoint())

    elif answer == "110":
        speak("say your context")
        usertext = take_input(self)
        system_task.note(usertext)
        return("taken note of that")     
 
    elif answer == "close notepad":
        k=system_task.close_notepad()
        return(k)   

    elif answer == "111":
        return ("i'm not sure about, may be you should give me some time")

    elif answer == "112":
        return ("it's hard to understand")

    elif answer == "on speak":
        return database.turn_on_speech()

    elif answer == "off speak":
        return database.turn_off_speech()

    elif answer == 'music':
        system_task.play_music()
        return "playing song"

    elif answer == 'video':
        system_task.videos()
        return ("playing video")

    elif answer == 'focus':
        return (system_task.play_focus())

    elif answer == 'photo':
        system_task.photo()
        return ("opening photo")

    elif answer == 'chrome':
        return (system_task.chrome())

    elif answer == 'close chrome':
        return (system_task.close_chrome())

    elif answer == 'sublime text':
        return (system_task.sublime_text())

    elif answer == 'close sublime text':
        return (system_task.close_sublime_text())

    elif answer == 'vs code':
        return (system_task.vs_code())

    elif answer == 'close vs code':
        return (system_task.close_vs_code())

    elif answer == 'shell':
        return (system_task.shell())

    elif answer == 'word':
        return (system_task.word())

    elif answer == 'close word':
        return (system_task.close_word())

    elif answer == 'excel':
        return (system_task.excel())

    elif answer == 'close excel':
        return (system_task.close_excel())

    elif answer == "open facebook":
        open_facebook()
        return "opening facebook"

    elif answer == "close facebook":
        close_facebook()
        return "closing facebook"

    elif answer == "open google":
        open_google()
        return "opening google"

    elif answer == "open spotify":
        open_spotify()
        return "opening spotify"

    elif answer == "open geeksforgeeks":
        open_gfg()
        return "opening geeks for geeks"

    elif answer=="open youtube":
        open_youtube()
        return("opening youtube")

    elif answer=="open wynk":
        open_wynk()
        return "opening wynk"

    elif answer=="open stackof":
        open_stackof()
        return "opening stack over flow"

    elif answer=="open git":
        open_git()
        return "opening github"

    elif answer=="comsites":
        responded=open_comsites(self)
        return (f"opening {responded}")

    elif answer=="sites":
        responded=open_sites(self)
        return (f"opening {responded}")

    elif answer=="image search":
        responded=imgsearch(quest)
        return (f"opening {responded}")
    
    elif answer=="search":
        responded=search(quest)
        return (f"showing results for {responded}")

    elif answer=="play":
        responded=play(quest)
        return (f"playing... {responded}")

    elif answer=="whatsapp":
        return(open_whatsapp(self))

    elif answer == 'change name':
        give_output("okay! what do you want to call me")
        temp = take_input(self)
        if temp == assistant_details.name:
            return "can't change. i think you're happy with my old name"
        else:
            database.update_name(temp)
            assistant_details.name=temp
            return "now you can call me "+ temp
    
    elif answer == "0":
        return "say again"

    elif answer == "turn off":
        return "signing off sir"
    else:
        try:
            res = client.query(quest)
            if res['@success']=='true':
                pod1=res['pod'][1]
                result = pod1['subpod']['plaintext']
                if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                    if result == '(data not available)':
                        answer = internet.check_on_wikipedia(quest+" wikipedia")
                        if answer!="":
                            return answer
                        else:
                            addq=adding_query(self,quest)
                            return addq
                    else:
                        return result
                else:
                    answer = internet.check_on_wikipedia(quest+" wikipedia")
                    if answer!="":
                        return answer
                    else:
                        addq=adding_query(self,quest)
                        return addq
            else:
                answer = internet.check_on_wikipedia(quest+" wikipedia")
                if answer!="":
                    return answer
                else:
                    addq=adding_query(self,quest)
                    return addq
        except Exception as e:
            return (e)