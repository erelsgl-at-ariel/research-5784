# A utility script to view the database.

import sqlite3
db = sqlite3.connect('flask_example/site.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM user")
print("user table: ")
for row in cursor:
    print("  ",row)
cursor.execute("SELECT * FROM post")
print("post table: ")
for row in cursor:
    print("  ",row)
