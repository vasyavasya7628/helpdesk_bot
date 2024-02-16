from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from database.db_methods import get_orders_waiting


def get_list_of_waiting(kb):
    data = get_orders_waiting()
    order_description = [data[3] for data in data]
    for i in range(len(order_description)):
        kb.button(text=order_description[i])
        kb.button(text="Yes")


def kb_waiting_reaction() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    get_list_of_waiting(kb)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
