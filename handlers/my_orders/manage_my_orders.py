import logging

from aiogram import Router
from aiogram.types import CallbackQuery

from data.db_methods import database_close_order

manage_my_orders_router = Router()


async def close_order(order_id, admin_id):
    logging.info("close")
    await database_close_order(order_id, admin_id)


async def delay_order(order_id, admin_id):
    logging.info("delay")
    await database_delay_order(order_id, admin_id)


async def update_order_status(data_order_and_id):
    if data_order_and_id[0] == "close":
        await close_order(data_order_and_id[1], data_order_and_id[2])
    elif data_order_and_id[0] == "delay":
        await delay_order(data_order_and_id[1], data_order_and_id[2])


@manage_my_orders_router.callback_query()
async def change_order_status(callback: CallbackQuery):
    data_order_and_id = callback.data.split("|")
    await update_order_status(data_order_and_id)
