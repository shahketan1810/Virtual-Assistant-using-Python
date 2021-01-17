import sqlite3
from internet import check_internet_connection

def create_connection():


    connection = sqlite3.connect("memory.db")
    return connection

def get_questions_and_answers():

    con = create_connection()
    cur = con.cursor()

    cur.execute('select * from questionsAndAnswers')

    return cur.fetchall()

def insert_question_and_answer(question,answer):
    con=create_connection()
    cur=con.cursor()
    #insert into tablename value ('question','answers')
    query="INSERT INTO questionsAndAnswers values('"+question+"','"+answer+"')"
    cur.execute(query)
    con.commit()

def get_answers_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if (row[0].lower()) in (question.lower()):
            answer = row[1]
            break
            
    return answer

def get_name():
    con=create_connection()
    cur=con.cursor()
    #insert into tablename value ('question','answers')
    query="select value from memory where name = 'assistant name'"
    cur.execute(query)
    return cur.fetchall()[0][0]

def update_name(new_name):
    con=create_connection()
    cur=con.cursor()
    #insert into tablename value ('question','answers')
    query="update memory set value = '"+new_name+"' where name = 'assistant name'"
    cur.execute(query)
    con.commit()
     
def update_last_seen(last_seen_date):
    con=create_connection()
    cur=con.cursor()
    #insert into tablename value ('question','answers')
    query="update memory set value = '"+str(last_seen_date)+"' where name = 'last seen date'"
    cur.execute(query)
    con.commit()   

def get_last_seen():
    con=create_connection()
    cur=con.cursor()
    #insert into tablename value ('question','answers')
    query="select value from memory where name = 'last seen date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])

def turn_on_speech():

    con=create_connection()
    cur=con.cursor()

    query="update memory set value = 'on' where name = 'speech'"
    cur.execute(query)
    con.commit()
    return ("speech turned on")


def turn_off_speech():
    con=create_connection()
    cur=con.cursor()
    
    query="update memory set value = 'off' where name = 'speech'"
    cur.execute(query)
    con.commit()    
    return ("ok i won't speak")    

def speak_is_on():
    con=create_connection()
    cur=con.cursor()

    query="select value from memory where name = 'speech'"
    cur.execute(query)
    ans=str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    else:
        return False