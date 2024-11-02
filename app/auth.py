import sqlite3

connection = sqlite3.connect('../database/rent.db')
cursor = connection.cursor()


def insert_users(username, email, number, password):
    cursor.execute('INSERT INTO users (username, email, number, password) VALUES (?, ?, ?, ?)',
                   (username, email, number, password))
    return cursor.lastrowid


def insert_house(name, place, price, people, animals, image_path=None):
    image_data = None
    if image_path:
        with open(image_path, 'rb') as file:
            image_data = file.read()

    cursor.execute('INSERT INTO houses (name, place, price, image) VALUES (?, ?, ?, ?)',
                   (name, place, price, image_data))
    return cursor.lastrowid


user_id = insert_users('test_name', 'test@gmail.com', '+380759910319', 'test123pass')
house_id = insert_house('Lakeview Apartment', 'Downtown', 1200, 'path/to/image.jpg')

connection.commit()
connection.close()


