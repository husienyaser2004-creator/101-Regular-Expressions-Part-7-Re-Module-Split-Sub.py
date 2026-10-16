#-----------------------------------------------
#-Databases - SQLite Create Skills App Part 2---
#-----------------------------------------------

# Import SQlite Module
import sqlite3

# Create Databasa and Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor 
cr = db.cursor()

# Commit and Close Method


def commit_and_close ():

    # Save (Commit) changes
    db.commit()

    # Close Database
    db.close()
    print("Connection To Databasa Is Closed")

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

    cr.execute(f"select * from skills where user_id = '{uid}'")

    results = cr.fetchall()

    print(f"You Have {len(results)} Skills.")

    if len (results) > 0:

        print("Showing Skills With Progress: ")

    for row in results:

        print(f"Skill => {row[0]},", end= " ")

        print(f"Progress => {row[1]}%")

    commit_and_close()


def add_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write Skill Progress ").strip()

    cr.execute(f"insert into skills(name, progress, user_id) Values('{sk}', '{prog}' , '{uid}')")

    commit_and_close()


def delete_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write Skill Progress ").strip()

    cr.execute(f"delete from skills where name =('{sk}' ")

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


else:

    print(f"Sorry This Command \"{user_input}\" Is Not Found")

          
