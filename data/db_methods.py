import logging
import os
import re

import aiosqlite

from res.resources import OrderStatus


def get_db_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "districts.db")


async def insert_user(district_id, user_id, user_name, user_firstname, user_lastname):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute(
                'INSERT INTO users (district_id, user_id, user_name, user_nickname, role) SELECT ?, ?, ?, ?, ?'
                'WHERE NOT EXISTS ('
                'SELECT 1 FROM users '
                'WHERE user_id = ?)',
                (district_id, user_id, user_name, f"{user_firstname} {user_lastname}", "admin", user_id))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function insert_user: {error}")


async def select_user_id(district_id):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute("SELECT user_id FROM users WHERE district_id = ?", (district_id,))
            data = await cursor.fetchall()
            return [row[0] for row in data]
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function select_user_id: {error}")


async def select_admins_same_district(admin_id):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute("SELECT district_id FROM users WHERE user_id = ?", (admin_id,))
            current_admin_district = await cursor.fetchone()

            if current_admin_district:
                current_district_id = current_admin_district[0]
                cursor = await conn.execute("SELECT user_id FROM users WHERE district_id = ?", (current_district_id,))
                return [row[0] for row in await cursor.fetchall()]
        return []
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function select_admins_same_district: {error}")


async def delete_admin(admin_id):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute("DELETE FROM users WHERE user_id = ?", (admin_id,))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function delete_admin: {error}")


async def add_order_info(district_id, order_number, order_description, from_user, data_time):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute('''INSERT INTO orders (district_id, user_problem_description, from_user, order_number,
            date_create, status) VALUES (?, ?, ?, ?, ?, ?)''',
                               (
                                   district_id, order_description, from_user, order_number, data_time,
                                   OrderStatus.WAITING.value))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function add_order_info: {error}")


async def add_worker(to_admin, order_number):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute('''UPDATE orders
                                  SET to_admin = ?
                                  WHERE order_number = ?''', (to_admin, convert_string_to_int(str(order_number))))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function add_worker: {error}")


def convert_string_to_int(input_string):
    return re.sub(r'\D', '', input_string)


async def store_order_number(order_number):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute("DELETE FROM order_number")
            await conn.execute("INSERT INTO order_number (order_number) VALUES (?)", (order_number,))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function store_order_number: {error}")


async def get_order_number():
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute("SELECT order_number FROM order_number")
            data = await cursor.fetchall()
            return [row[0] for row in data]
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function store_order_number: {error}")


async def get_order_info(district_id):
    try:
        await clear_db()
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute("SELECT * FROM orders WHERE district_id = ? ORDER BY id DESC LIMIT 10;",
                                        (district_id,))
            results = await cursor.fetchall()
            logging.info(results)
        return list(results)
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function get_order_info: {error}")


async def clear_db():
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute('SELECT COUNT(*) FROM orders')
            count = (await cursor.fetchone())[0]
            if count > 1000:
                await conn.execute('''
                                   DELETE FROM orders
                                   WHERE id NOT IN (
                                       SELECT id FROM orders
                                       ORDER BY id DESC
                                       LIMIT ?
                                   )
                                   ''', (count // 2,))
                await conn.commit()

    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function clear_db: {error}")


def check_none_string(text):
    return "" if text is None else text
