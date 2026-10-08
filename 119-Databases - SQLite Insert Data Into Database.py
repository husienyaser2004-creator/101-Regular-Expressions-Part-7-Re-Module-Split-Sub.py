#----------------------------------------------------------------
#------Databases - SQLite Insert Data Into Database--------------
#----------------------------------------------------------------
# Cursor => All Operations IN SQl Done By Cursor Not The Connection Itself
# Commit => Save All Changes 
#-----------------------------------------------------------------
# import Sqlite3 Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Create The Table and Fields
cr = db.cursor()
cr.execute("create table if not exists users (user_id integer, name text)")

cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Inserting Data Into Table
#cr.execute("insert into users(user_id, name) Values(1, 'Hussien')")
#cr.execute("insert into users(user_id, name) Values(2, 'Ali')")
#cr.execute("insert into users(user_id, name) Values(3, 'Noha')")

my_list = ["Hussien", "Yasser", "Soudy", "Mohamed", "Leen", "Rahama", "Sanaa"]

for Key, user in enumerate(my_list):

    cr.execute(f"insert into users(user_id, name) Values({Key + 1}, '{user}')")

# Save (commit) the Changes
db.commit()

# Close The Database
db.close()
