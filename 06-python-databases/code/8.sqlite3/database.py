import sqlite3
# Connect to database
db = sqlite3.connect('my_database.db')

# Get a cursor
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE users(
        id INTEGER PRIMARY KEY, 
        name TEXT,
        phone TEXT, 
        email TEXT unique, 
        password TEXT)
''')
db.commit()


name1 = 'Tom Pythonovitz'
phone1 = '3366858'
email1 = 'Tom.Pythonovitz@example.com'
# A very secure password
password1 = '12345'
 
name2 = 'Tammi Pythonovitz'
phone2 = '5557241'
email2 = 'Tammi@example.com'
password2 = 'TammiLoveTom'

name3 = 'George Rustniovsky'
phone3 = '33333'
email3 = 'GRust@example.com'
password3 = 'Rust for ever'
 
# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
print('First user inserted')
 
# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
print('Second user inserted')
db.commit()

# Insert user 3
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(:name,:phone, :email, :password)''',
                  {'name':name3, 'phone':phone3, 'email':email3, 'password':password3})
print('Third user inserted')
db.commit()

users = [('Joee Javany', '2222','joo@example.mail','password'),
        ('Shirel Cplustik', '3333','cpp@example.mail','cppass'),
        ('Adam Kotlinernberg', '4444','Adam_Kotlin@example.mail','JustPassword')
        ]
# Insert many
cursor.executemany('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', users)
print('Many users inserted')
db.commit()


cursor.execute('''SELECT name, email, phone FROM users''')
all_rows = cursor.fetchall()
print()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

print()
cursor.execute('''SELECT name, password FROM users''')
for row in cursor:
    print(f'{row[0]} : {row[1]}')


cursor.execute('''SELECT name, email, phone 
                FROM users WHERE name=?''',(name1,) )
print(cursor.fetchall())

# Update user with id 1
newphone = '3113093164'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
 (newphone, userid))
# Delete user with id 2
delete_userid = 2
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
db.commit()

print()
cursor.execute('''SELECT name,phone  FROM users''')
for index ,row in enumerate(cursor):
    print(f'{index} ) {row[0]} : {row[1]}')


cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''',
("121212", userid))
# The user's phone is not updated
db.rollback()


# To drop the table:
cursor.execute('''
    DROP TABLE users
''')
db.commit()

db.close()