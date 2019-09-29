# Python MySQL Database Access - Example Program

import MySQLdb

db = MySQLdb.connect("localhost", "checkuser", "checkpass123", "MYDATABASE")  # this opens database connection

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version: %s " % data)

db.close()  # this disconnect from the server