import sqlite3
import os
from res.resources import get_districts

# Подключение к базе данных (если она существует) или создание новой
conn = sqlite3.connect('districts.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS districts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district_name TEXT NOT NULL
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district_id INTEGER,
                    user_id INTEGER,
                    user_name TEXT,
                    user_nickname TEXT,
                    role TEXT,
                    FOREIGN KEY (district_id) REFERENCES district (id)
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district_id INTEGER,
                    order_number INTEGER,
                    user_problem_description TEXT,
                    admin_comment Text,
                    from_user TEXT,
                    to_admin TEXT,
                    date_create TEXT,
                    time_taken,
                    date_close TEXT,
                    status TEXT,
                    FOREIGN KEY (district_id) REFERENCES district (id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS order_number (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_number INTEGER
                )''')

if os.path.exists("districts.db"):
    conn.commit()
    conn.close()
else:
    districts = get_districts()

    for i in range(0, len(districts), 2):
        district_name = districts[i]
        user_id = districts[i + 1]
        cursor.execute('INSERT INTO districts (district_name) VALUES (?)', (district_name,))
        district_id = cursor.lastrowid

    cursor.execute("INSERT INTO order_number (order_number) VALUES (1)")
    conn.commit()
    conn.close()
