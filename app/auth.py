import sqlite3

connection = sqlite3.connect('./database/rent.db')
cursor = connection.cursor()

def insert_users(username, email, number, password):
    try:
        cursor.execute('INSERT INTO users (username, email, number, password) VALUES (?, ?, ?, ?)',
                       (username, email, number, password))
        connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error inserting user:", e)
        return None

def insert_house(name, place, region, price, people, animals, image_url, booked):
    try:
        cursor.execute('INSERT INTO houses (name, place, region, price, people, animals, image, booked) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (name, place, region, price, people, animals, image_url, booked))
        connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print("Error inserting house:", e)
        return None

def verify_us(email, password):
    try:
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        return user
    except sqlite3.Error as error:
        print("Verification error:", error)
        return None

def set_booked_status(booked, name=None, place=None, region=None):
    try:
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

# Example usage
# user_id = insert_users('test_name', 'test@gmail.com', '+380759910319', 'test123pass')
# house_id = insert_house('TestApartment', 'TestPlace', 'Dnipro', 1200, 10, True, 'http://example.com/image.jpg', False)
set_booked_status(True, name="TestApartment", place="TestPlace")

# Close the connection
connection.commit()
connection.close()
