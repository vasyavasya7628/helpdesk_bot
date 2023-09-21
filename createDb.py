import sqlite3

# Создайте или подключитесь к базе данных SQLite (если файл не существует, он будет создан)
conn = sqlite3.connect('districts.db')

# Создайте курсор для выполнения операций с базой данных
cursor = conn.cursor()

# Создайте таблицу для хранения данных, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS districts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        code TEXT
    )
''')

# Список данных
districts = [
    "Контакт Центр",
    "12452124",
    "Отдел 'Мои документы' Беловский район",
    "12452124",
    # Вставьте остальные данные здесь
]

# Разделите список данных на записи (каждая запись - это пара name и code)
records = [(districts[i], districts[i + 1]) for i in range(0, len(districts), 2)]

# Вставьте записи в таблицу
cursor.executemany('INSERT INTO districts (name, code) VALUES (?, ?)', records)

# Сохраните изменения в базе данных
conn.commit()

# Закройте соединение с базой данных
conn.close()
