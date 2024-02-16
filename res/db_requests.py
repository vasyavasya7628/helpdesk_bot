import logging
from enum import Enum

import psycopg2

from res.secret import DatabaseOp as connData


class DatabaseRequests(Enum):
    CREATE_USERS = '''CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        district_id INTEGER,
                        user_id INTEGER,
                        user_name TEXT,
                        user_nickname TEXT,
                        role TEXT,
                        FOREIGN KEY (district_id) REFERENCES districts (id)
                     )'''
    CREATE_DISTRICTS = '''CREATE TABLE IF NOT EXISTS districts (
                        id SERIAL PRIMARY KEY,
                        district_name TEXT NOT NULL
                     )'''
    CREATE_ORDER_NUMBER = '''CREATE TABLE IF NOT EXISTS order_number (
                        id SERIAL PRIMARY KEY,
                        order_number INTEGER
                    )'''
    CREATE_ORDERS = '''CREATE TABLE IF NOT EXISTS orders (
                        id SERIAL PRIMARY KEY,
                        district_id INTEGER,
                        order_number INTEGER,
                        user_problem_description TEXT,
                        admin_comment TEXT,
                        from_user TEXT,
                        to_admin TEXT,
                        date_create TIMESTAMP,
                        time_taken TIMESTAMP,
                        date_close TIMESTAMP,
                        status TEXT,
                        admin_telegram_id INTEGER,
                        FOREIGN KEY (district_id) REFERENCES districts (id)
                    )'''


def postgres_connect():
    return psycopg2.connect(
        dbname=connData.DATABASE.value,
        user=connData.USER.value,
        password=connData.PASSWORD.value,
        host=connData.HOST.value,
        port=connData.PORT.value
    )


def table_exists(conn, table_name):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM %s;", (table_name,))
        result = cur.fetchone()
        print(f"{result}")
        return None if result == 0 else result
