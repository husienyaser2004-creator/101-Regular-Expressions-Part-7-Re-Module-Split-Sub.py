#------------------------------------------------------
#----Databases - SQLite Retrieve Data From Database----
#------------------------------------------------------
#-- fetchone => returns a single record or None if no more are available
#-- fetchall => fetches all the rows of a query result It returns all the rows
#------ as a list of tuples An empty list is returned if there is no record to fetch
#--fetchmany (size) =>
#------------------------------------------------------------------------------------

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

# Fetch Data 
cr.execute("select name from users")

#print(cr.fetchone())
#print(cr.fetchone())
#print(cr.fetchone())

#print(cr.fetchall())

print(cr.fetchmany(3))

# Save (commit) the Changes
db.commit()

# Close The Database
db.close()
