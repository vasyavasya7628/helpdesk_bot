import logging

from aiogram import Router
from aiogram.types import CallbackQuery

from data.db_methods import change_status, find_my_orders
from res.resources import OrderDatabaseActions

manage_my_orders_router = Router()


def order_number():
    return


@manage_my_orders_router.callback_query()
async def change_order_status(callback: CallbackQuery):
    data_order_and_id = callback.data.split("|")
    delete_zero_item = data_order_and_id.pop(0)
    my_orders = await find_my_orders(data_order_and_id[1], data_order_and_id[2])
    if data_order_and_id[0].__contains__(OrderDatabaseActions.CLOSE.value) and delete_zero_item == my_orders:
        await change_status(data_order_and_id[1], data_order_and_id[2])
        logging.info("Заявка закрыта")
    elif data_order_and_id[0].__contains__(OrderDatabaseActions.DELAY.value):
        await change_status(data_order_and_id[1], data_order_and_id[2])
        logging.info("Заявка отложена")
