from aiogram.types import ReplyKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import write_to_it, order_list, my_orders, active_orders


def get_my_orders() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=order_list())
    kb.button(text=my_orders())
    kb.button(text=active_orders())
    kb.button(text=write_to_it())

    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
