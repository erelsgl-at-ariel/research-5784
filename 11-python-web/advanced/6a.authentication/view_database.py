# A utility script to view the database.

import sqlite3
db = sqlite3.connect('flask_example/site.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM user")
all_rows = cursor.fetchall()
print(all_rows)
