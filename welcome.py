from time_module import get_hours,get_date
from output_module import give_output
import database 


def greet():

    #fetch previous date
    previous_date = database.get_last_seen()

    #fetch today's date and store it to database
    today_date = get_date()
    database.update_last_seen(today_date)

    
    if previous_date == today_date: 
        return("welcome back sir")
    
    else:
        hour = int(get_hours())
        if hour>=0 and hour<12:
            return("Good Morning! sir")

        elif hour>=12 and hour<18:
            return(" Good Afternoon! sir")   

        else:
            return(" Good Evening! sir")      