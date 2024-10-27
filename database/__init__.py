import sqlite3

with sqlite3.connect('rent.db') as db:
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY NOT NULL,
    username VARCHAR(255),
    email VARCHAR(255),
    number VARCHAR(255),
    password VARCHAR(255));
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(255),
    place VARCHAR(255),
    price INTEGER NOT NULL);   
    """)

