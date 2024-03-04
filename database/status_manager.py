import logging

from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from database.db_methods import database_close_order, database_delay_order, database_get_order

manage_my_orders_router = Router()


async def close_order(order_id, admin_id):
    logging.info("close")
    await database_close_order(order_id, admin_id)


async def delay_order(order_id, admin_id):
    logging.info("delay")
    await database_delay_order(order_id, admin_id)


async def get_order(order_id, admin_id):
    logging.info("get_order")
    return await database_get_order(order_id, admin_id)


async def update_order_status(data_order_and_id):
    if data_order_and_id[0] == "close":
        await close_order(data_order_and_id[2], data_order_and_id[1])
    elif data_order_and_id[0] == "delay":
        await delay_order(data_order_and_id[2], data_order_and_id[1])
    elif data_order_and_id[0] == "get_order":
        return await get_order(data_order_and_id[2], data_order_and_id[1])


@manage_my_orders_router.callback_query()
async def change_order_status(callback: CallbackQuery, bot: Bot):
    data_order_and_id = callback.data.split("|")
    value = await update_order_status(data_order_and_id)
    if value is False:
        await bot.answer_callback_query(callback.id, "Заявку забрали", show_alert=True)
