#----------------------------------------------------------
#---- Databases - SQLite Update And Delete From Database---
#----------------------------------------------------------

# Import SQlite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# setting up the Cursor
cr = db.cursor()

# Update Data
cr.execute("update users set name = 'Ahmed' where user_id = 1")
cr.execute("update users set name = 'Mohamed' where user_id = 2")
cr.execute("update users set name = 'Ali' where user_id = 3")
cr.execute("update users set name = 'sayed' where user_id = 4")
cr.execute("update users set name = 'Ameer' where user_id = 5")

# Dalete Data
cr.execute("delete from users Where user_id = 5")


# Fetch Data 
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (Commit) changes
db.commit()

# Close Database
db.close()