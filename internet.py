import socket
import wikipedia

def check_internet_connection():

    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
        return False        
    else:
       return True

def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace("who is","")
    query = query.replace("what is","")
    query = query.replace("do you know","")
    query = query.replace("tell me about","")

    query =query.strip()

    try:
        data=wikipedia.summary(query,sentences=2)
        return data 
    except Exception :
        return ""