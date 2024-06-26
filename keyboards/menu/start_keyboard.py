from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import Text


def get_kb_start(tg_user_id=False) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    if tg_user_id:
        kb.button(text=Text.ORDER_LIST.value)
        kb.button(text=Text.MY_ORDERS.value)
        kb.button(text=Text.ACTIVE_ORDERS.value)
        kb.button(text=Text.WRITE_TO_IT.value)
    else:
        kb.button(text=Text.WRITE_TO_IT.value)

    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


