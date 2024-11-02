import sqlite3

# Establish a connection to the database
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

def insert_house(name, place, price, people, animals, image_path=None):
    try:
        # Set image_data to None by default
        image_data = None
        if image_path:
            with open(image_path, 'rb') as file:
                image_data = file.read()

        # Insert house details, including people and animals fields
        cursor.execute('INSERT INTO houses (name, place, price, people, animals, image) VALUES (?, ?, ?, ?, ?, ?)',
                       (name, place, price, people, animals, image_data))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error inserting house:", e)
        return None


user_id = insert_users('test_name', 'test@gmail.com', '+380759910319', 'test123pass')
house_id = insert_house('TestApartment', 'TestPlace', 1200, 10, True, 'path/to/image.jpg')

connection.commit()
connection.close()


