from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import res.resources as res


def get_kb_return() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=res.return_to_main_menu())
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
