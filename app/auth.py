import sqlite3

connection = sqlite3.connect('../database/rent.db')
cursor = connection.cursor()

def insert_users(username, email, number, password):
    try:
        cursor.execute('INSERT INTO users (username, email, number, password) VALUES (?, ?, ?, ?)',
                       (username, email, number, password))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error inserting user:", e)
        return None

def insert_house(name, place, region, price, people, animals, image_path=None):
    try:
        image_data = None
        if image_path:
            with open(image_path, 'rb') as file:
                image_data = file.read()

        cursor.execute('INSERT INTO houses (name, place, region, price, people, animals, image) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (name, place, region, price, people, animals, image_data))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error inserting house:", e)
        return None

def verify_us(email, password):
    try:
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        if user:
            return user
        else:
            return None
    except sqlite3.Error as error:
        print("Verification error", error)
        return None



user_id = insert_users('test_name', 'test@gmail.com', '+380759910319', 'test123pass')
house_id = insert_house('TestApartment', 'TestPlace', 'Dnipro', 1200, 10, True, None)

connection.commit()
connection.close()


