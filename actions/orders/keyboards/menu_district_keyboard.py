from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from actions.user.keyboard.user_districts_kb import list_to_buttons


def kb_menu_districts() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню")
    list_to_buttons(kb, "💼")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
