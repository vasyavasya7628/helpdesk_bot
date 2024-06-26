import logging
import os
import re
import sqlite3

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
            cursor = await conn.execute("SELECT user_id FROM users;")
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
                current_district_id = None
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


async def get_admins():
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute("SELECT user_id FROM users;")
            data = await cursor.fetchall()
            return [item[0] for item in data]
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function add_order_info: {error}")


async def add_order_info(order_number, order_description, from_user, data_time):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute('''INSERT INTO orders (user_problem_description, from_user, order_number,
            date_create, status) VALUES (?, ?, ?, ?, ?)''',
                               (
                                   order_description, from_user, order_number, data_time,
                                   OrderStatus.WAITING.value))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function add_order_info: {error}")


async def add_worker(to_admin, order_number, admin_telegram_id):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            await conn.execute('''UPDATE `orders`
                                  SET to_admin = ?,
                                      admin_telegram_id = ?
                                  WHERE order_number = ?''',
                               (to_admin, admin_telegram_id, convert_string_to_int(str(order_number))))
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
            logging.info(f"{[row[0] for row in data]}")
            return [row[0] for row in data]
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function store_order_number: {error}")


async def change_order_status(order_number, new_status):
    try:
        db_path = get_db_path()
        async with aiosqlite.connect(db_path) as conn:
            await conn.execute("UPDATE `orders` SET status = ? WHERE order_number = ?", (new_status,
                                                                                         convert_string_to_int(
                                                                                             str(order_number))))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.error(f"[ERROR] in function change_order_status: {error}")


async def check_role(user_id):
    try:
        db_path = get_db_path()
        async with aiosqlite.connect(db_path) as conn:
            cursor = await conn.execute("SELECT * FROM `users` WHERE user_id = ? AND role=\"admin\";",
                                        (user_id,))
            result = await cursor.fetchone()
            return bool(result)
    except aiosqlite.Error as error:
        logging.error(f"[ERROR] in function check_role: {error}")


async def get_order_info():
    try:
        await clear_db()
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute(
                "SELECT * FROM orders ORDER BY id;")
            results = await cursor.fetchall()
            logging.info(results)
        return list(results)
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function get_order_info: {error}")


# ну костыль да, но это работает. Синхронный запрос в синхронную функцию.
# Потому что результат асинхронной функции в синхронную не работает
def get_orders_waiting():
    try:
        with sqlite3.connect(get_db_path()) as conn:
            cursor = conn.execute(
                "SELECT * FROM orders WHERE status = ?;",
                (OrderStatus.WAITING.value,))
            results = cursor.fetchall()
            logging.info(f"get_orders_waiting: {results}")
        return list(results)
    except sqlite3.Error as error:
        logging.info(f"[ERROR] in function get_order_info: {error}")


async def find_orders(order_id, admin_id):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute(
                "SELECT order_number, admin_telegram_id FROM orders WHERE order_number = ? AND admin_telegram_id = ?",
                (admin_id, order_id))
            results = await cursor.fetchall()
            logging.info(results)
            logging.info(f"[RESULT] in function find_orders: {[i[0] for i in results]}")
        return [i[0] for i in results]
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function get_order_info: {error}")


async def database_close_order(order_id, admin_id):
    order_id = order_id
    admin_id = admin_id
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            logging.info(f"database_close_order: order_id = {order_id} admin_id = {admin_id}")
            await conn.execute(
                "UPDATE `orders` SET status =\"закрыта\", admin_telegram_id =\"\" "
                "WHERE order_number = ? AND admin_telegram_id = ?;",
                (order_id, admin_id))
            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function database_close_order: {error}")


async def database_delay_order(order_id, admin_id):
    order_id = order_id
    admin_id = admin_id
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            logging.info(f"database_close_order: order_id = {order_id} admin_id = {admin_id}")
            await conn.execute(
                "UPDATE `orders` SET status =\"отложена\", admin_telegram_id =\"\" "
                "WHERE order_number = ? AND admin_telegram_id = ?;",
                (order_id, admin_id))

            await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function database_close_order: {error}")


async def database_get_order(order_id, admin_id):
    order_id = order_id
    admin_id = admin_id
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            logging.info(f"database_close_order: order_id = {order_id} admin_id = {admin_id}")
            cursor = await conn.execute("SELECT 1 FROM `orders` WHERE status != \"в работе\" and order_number=?;",
                                        (order_id,))
            id_found = await cursor.fetchone()
            logging.info(f"ПОЧЕМУ НЕ МОГУ ВЗЯТЬ ЗАЯВКУ {id_found}")
            if id_found is None:
                logging.info("Заявку уже забрали")
                return False
            else:
                await conn.execute(
                    "UPDATE `orders` SET status =\"в работе\", admin_telegram_id=?"
                    "WHERE order_number = ?;",
                    (admin_id, order_id))
                await conn.commit()
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function database_close_order: {error}")


async def clear_db():
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute('SELECT COUNT(*) FROM orders')
            count = (await cursor.fetchone())[0]
            if count > 10000:
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


async def sync_get_order_info(admin_telegram_id="None"):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute(
                "SELECT * FROM orders WHERE admin_telegram_id = ?;",
                (admin_telegram_id,))
            results = await cursor.fetchall()
            logging.info(results)
            return list(results)
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function get_order_info: {error}")


async def order_info(admin_telegram_id="None"):
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute(
                "SELECT * FROM orders WHERE status !=\"закрыта\" and status !=\"в работе\";")
            results = await cursor.fetchall()
            logging.info(results)
            return list(results)
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function get_order_info: {error}")


def check_none_string(text):
    return "" if text is None else text
