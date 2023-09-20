from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_kb_start() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🏻‍💻 Написать в IT-Отдел")
    kb.button(text="Узнать свой ID")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
