#---------------------------------------------------
#-- Databases - SQLite Create Skills App Part 3-----
#---------------------------------------------------

# Import SQlite Module
import sqlite3

# Create Databasa and Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor 
cr = db.cursor()

# Commit and Close Method

def commit_and_close():
    """ Commit Changes and Close Connection To Database"""
    db.commit()    # Save (Commit) Change
    db.close()     # Close Database
    print("Connection To Database Is Closed")

# My User ID
uid = 2

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()


# Command List
Commands_list = ["s","a","d","u","q"]


# Define The Methods 

def show_skill():

    cr.execute(" select * from skills")

    commit_and_close()


def add_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write Skill Progress ").strip()

    cr.execute(f"insert into skills(name, progress, user_id) Values('{sk}', '{prog}', '{uid}')")

    commit_and_close()


def delete_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    #prog = input("Write Skill Progress ").strip()

    cr.execute(f"delete from skills where name =('{sk}' and user_id = '{uid}'")

    commit_and_close()


def update_skill():

    print("update skill Progress") 

    commit_and_close()

# Check If Command Is Exists
if user_input in Commands_list:

   # print(f"Commands Found {user_input}")

    if user_input == "s":

        show_skill()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()

    else :           

        print("App Is Closed")

        commit_and_close


else:

    print(f"Sorry This Command \"{user_input}\" Is Not Found")

