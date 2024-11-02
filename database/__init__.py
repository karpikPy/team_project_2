import sqlite3

def create_db():
    try:
        with sqlite3.connect('rent.db') as db:
            cursor = db.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                number TEXT,
                password TEXT NOT NULL
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS houses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                place TEXT,
                region TEXT,
                people INTEGER NOT NULL,
                animals BOOLEAN,
                image BLOB,
                price INTEGER NOT NULL
            );
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS booked (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                house_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (house_id) REFERENCES houses(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
            """)

        print("Database and tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", e)


create_db()

