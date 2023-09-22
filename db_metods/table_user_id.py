import os.path
import sqlite3


def insert_user(district_id, user_id):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "districts.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO user_id (district_id, user_id_number) SELECT ?, ? WHERE NOT EXISTS (SELECT 1 FROM user_id WHERE user_id_number = ?)',
        (district_id, user_id, user_id))

    conn.commit()
    conn.close()


def get_user_id():
    conn = sqlite3.connect('districts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT district_id, user_id_number FROM user_id')
    data = cursor.fetchall()
    data_list = []
    for row in data:
        data_list.append(row)
    conn.commit()
    conn.close()
