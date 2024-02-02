from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import Text


def admin_register_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=Text.RETURN_TO_MAIN_MENU.value)
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
