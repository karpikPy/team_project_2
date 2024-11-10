import sqlite3

def connect_db(name_db="./database/rent.db"):
    conn = sqlite3.connect(name_db)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn, cursor

def closing(conn):
    conn.close()

def houses():
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM houses")
    houses = cursor.fetchall()
    closing(conn)
    return houses

def users():
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    closing(conn)
    return users

def id_user(id):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    user = cursor.fetchone()
    closing(conn)
    return user



def booked():
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM booked")
    booking = cursor.fetchone()
    closing(conn)
    return booking

