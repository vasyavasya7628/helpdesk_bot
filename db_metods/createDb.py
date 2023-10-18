import sqlite3

from res.resources import get_districts

# Подключение к базе данных (если она существует) или создание новой
conn = sqlite3.connect('../db_metods/districts.db')
cursor = conn.cursor()

# Создание таблицы для районов (district)
cursor.execute('''CREATE TABLE IF NOT EXISTS districts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district_name TEXT NOT NULL
                 )''')

# Создание таблицы для идентификаторов пользователей (user_id)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district_id INTEGER,
                    user_id INTEGER,
                    user_name TEXT,
                    user_nickname TEXT,
                    FOREIGN KEY (district_id) REFERENCES district (id)
                 )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    district_id INTEGER,
                    order_number INTEGER,
                    order_description TEXT,
                    from_user TEXT,
                    who_take_order TEXT,
                    time TEXT,
                    FOREIGN KEY (district_id) REFERENCES district (id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS order_number (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_number INTEGER
                )''')

districts = get_districts()

for i in range(0, len(districts), 2):
    district_name = districts[i]
    user_id = districts[i + 1]
    cursor.execute('INSERT INTO districts (district_name) VALUES (?)', (district_name,))
    district_id = cursor.lastrowid

cursor.execute("INSERT INTO order_number (order_number) VALUES (1)")
conn.commit()
conn.close()
