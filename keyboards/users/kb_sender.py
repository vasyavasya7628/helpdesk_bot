from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import Text


def kb_sender_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=Text.SEND_YES.value)
    kb.button(text=Text.SEND_NO.value)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
