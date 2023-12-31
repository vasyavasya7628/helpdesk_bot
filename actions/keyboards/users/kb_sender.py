from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def kb_sender_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Да✅")
    kb.button(text="Нет❌")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
