from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.users.user_districts_kb import list_to_buttons
from res.resources import Text


def kb_menu_districts() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=Text.MENU.value)
    list_to_buttons(kb, "💼")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
