import sqlite3
from check_for_the_question import find_similar_question
def create_connection():
    connection = sqlite3.connect("assistant.db")
    return connection

def get_questions_and_answers(tableName):

    con = create_connection()

    cursor = con.cursor()

    cursor.execute(f"select *from {tableName}")
    val = cursor.fetchall()
    cursor.close()
    con.close()
    return val

def get_value_from_memory(question):

    rows = get_questions_and_answers('questionAndAnswers')
    answer = ""
    
    newQue = find_similar_question(question,list(map(lambda x:x[0],rows)))

    for row in rows:
        if row[0].lower() in newQue.lower():
            answer= row[1]
            break
    return answer

def get_value_of_specified(name):
    rows = get_questions_and_answers('memory')
    answer = ""

    for row in rows:
        if row[0] == name:
            answer = row[1]
            break;
    return answer

def change_value_of_specified(name,value):
    # print(name)
    # print(value)
    # print(f"UPDATE memory SET value = {value} WHERE name = {name}")
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"UPDATE memory SET value = ? WHERE name = ?",
                   (value, name))
    
    con.commit()
    con.close()

def add_value_of_specified(name,value):
    con = create_connection()
    cursor = con.cursor()
    print(f"insert into memory values({value} ,{name})")
    cursor.execute(f"insert into memory values(? ,?)",
                   (value, name))
    
    con.commit()
    con.close()

# get_value_from_memory('can you tell me the exact time')