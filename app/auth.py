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

def insert_house(name, place, region, price, people, animals, image_path, booked):
    try:
        image_data = None
        if image_path:
            with open(image_path, 'rb') as file:
                image_data = file.read()

        cursor.execute('INSERT INTO houses (name, place, region, price, people, animals, image, booked) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, place, region, price, people, animals, image_data, booked))
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error inserting house:", e)
        return None


def set_booked_status(booked, name=None, place=None, region=None):
    try:
        # Build query to find house based on provided criteria
        query = "SELECT id FROM houses WHERE "
        criteria = []
        params = []

        if name:
            criteria.append("name = ?")
            params.append(name)
        if place:
            criteria.append("place = ?")
            params.append(place)
        if region:
            criteria.append("region = ?")
            params.append(region)

        # Join criteria with AND to match all provided fields
        query += " AND ".join(criteria)

        # Execute query to find the house
        cursor.execute(query, params)
        result = cursor.fetchone()

        if result is None:
            print("No house found with the specified criteria.")
            return

        house_id = result[0]

        # Update booked status in the database
        cursor.execute("UPDATE houses SET booked = ? WHERE id = ?", (booked, house_id))
        connection.commit()

        print(f"House '{name}' booking status set to {booked}.")

    except sqlite3.Error as e:
        print("Error setting booking status:", e)



#user_id = insert_users('test_name', 'test@gmail.com', '+380759910319', 'test123pass')
#house_id = insert_house('TestApartment', 'TestPlace', 'Dnipro', 1200, 10, True, None, False)
set_booked_status(True, name="TestApartment", place="TestPlace")
connection.commit()
connection.close()


