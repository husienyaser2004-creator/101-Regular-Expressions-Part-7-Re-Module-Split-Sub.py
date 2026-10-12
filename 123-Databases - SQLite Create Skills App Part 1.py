#----------------------------------------------------------
#---Databases - SQLite Create Skills App Part 1------------
#----------------------------------------------------------

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

    print("Show Skill")


def add_skill():

    print("Add Skill")


def delete_skill():

    print("Delete Skill")


def update_skill():

    print("update_skill")        


# Check If Command Is Exists
if user_input in Commands_list:

    print(f"Commands Found {user_input}")

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
