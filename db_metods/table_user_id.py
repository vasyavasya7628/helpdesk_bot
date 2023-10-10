import os.path
import sqlite3


def insert_user(district_id, user_id, user_name, user_firstname, user_lastname):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "districts.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO users (district_id, user_id, user_name, user_nickname) SELECT ?, ?, ?, ? WHERE NOT EXISTS ('
        'SELECT 1 FROM users '
        'WHERE user_id = ?)',
        (district_id, user_id, user_name, f"{user_firstname} {user_lastname}", user_id))

    conn.commit()
    conn.close()


def select_user_id(district_id):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "districts.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE district_id = ?", (district_id,))
    data = cursor.fetchall()
    data_list = [row[0] for row in data]
    conn.commit()
    conn.close()
    return data_list


def select_admins_same_district(admin_id):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "districts.db")

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Get the current admin's district
        cursor.execute("SELECT district_id FROM users WHERE user_id = ?", (admin_id,))
        current_admin_district = cursor.fetchone()

        if current_admin_district:
            current_district_id = current_admin_district[0]

            # Find other admins with the same district
            cursor.execute("SELECT user_id FROM users WHERE district_id = ?", (current_district_id,))
            other_admins = [row[0] for row in cursor.fetchall()]

            return other_admins

    return []


def delete_admin_from_db(admin_id):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "districts.db")

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Delete all info the current admin's district
        cursor.execute("DELETE FROM users WHERE user_id = ?", (admin_id,))
