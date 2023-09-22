from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import res.resources as res


def get_kb_reg_success() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=res.text_register_complete())
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
