from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def kb_sender_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да✅")
    kb.button(text="Нет❌")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
