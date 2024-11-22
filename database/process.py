import sqlite3

connection = sqlite3.connect('./database/rent.db', check_same_thread=False)
cursor = connection.cursor()

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

def get_house_id(house_id):
    conn, cursor = connect_db()
    try:
        cursor.execute("SELECT * FROM houses WHERE id = ?", (house_id,))
        house = cursor.fetchone()
        return house if house else None
    except sqlite3.Error as e:
        print(f"Error fetching house with ID {house_id}: {e}")
        return None
    finally:
        closing(conn)

def get_house_info(id):
    conn, cursor = connect_db()
    try:
        cursor.execute("SELECT * FROM houses WHERE id = ?", (id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error fetching house info: {e}")
        return None
    finally:
        closing(conn)
