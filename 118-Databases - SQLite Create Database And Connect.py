#-------------------------------------------------------
#--- Databases - SQLite Create Database And Connect ----
#-------------------------------------------------------
#- Create 
#- Execute 
#- Close
#--------------------------------------------------------

# import Sqlite3 Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Create The Table and Fields

db.execute("create table if not exists skills (name text, progress integer, user_id integer)")

# Close The Database
db.close()
