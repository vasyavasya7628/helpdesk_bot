from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import Text


def kb_cancel_message() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=Text.EXIT_TO_MENU.value)
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
