import sqlite3  #To use SQLite, we must import sqlite3.

# connecting to the database
connection = sqlite3.connect("example.db")
 
# cursor
crsr = connection.cursor()
 
# print statement will execute if there
# are no errors
print("Connected to the database")
 
# close the connection
connection.close()
