import sqlite3


def insert_user_id(district_id, user_id):
    # Подключение к базе данных (если она существует) или создание новой
    conn = sqlite3.connect('districts.db')
    cursor = conn.cursor()
    # Вставляем данные в таблицу user_id
    cursor.execute('INSERT INTO user_id (district_id, user_id_number) VALUES (?, ?)', (district_id, user_id))
    # Сохраняем изменения и закрываем соединение
    conn.commit()
    conn.close()
