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
districts = get_districts()
# Пример вставки данных из вашего списка districts
for i in range(0, len(districts), 2):
    district_name = districts[i]
    user_id = districts[i + 1]

    # Вставляем данные в таблицу district
    cursor.execute('INSERT INTO districts (district_name) VALUES (?)', (district_name,))

    # Получаем ID вставленной записи
    district_id = cursor.lastrowid

    # Вставляем данные в таблицу user_id
    # cursor.execute('INSERT INTO users (district_id, user_id) VALUES (?, ?)', (district_id, user_id))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
