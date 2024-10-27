import sqlite3

connection = sqlite3.connect('../database/rent.db')
cursor = connection.cursor()

def insert_users(username, email, number, password):
    cursor.execute('INSERT INTO users (username, email, number, password) VALUES (?, ?, ?, ?)',
                   (username, email, number, password))
    return cursor.lastrowid

user_id = insert_users('test_name', 'test@gmail.com', '+380759910319', 'test123pass')
connection.commit()
connection.close()