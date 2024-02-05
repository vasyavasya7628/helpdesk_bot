import logging

from aiogram import Router
from aiogram.types import CallbackQuery

manage_my_orders_router = Router()


def order_number():
    return


@manage_my_orders_router.callback_query()
async def change_order_status(callback: CallbackQuery):
    if int(callback.data) == order_number(int(callback.data)):

        logging.info(f"{callback.data}")
    else:
        logging.info(f"{callback.data}")
