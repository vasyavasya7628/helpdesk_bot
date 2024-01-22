from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from res.resources import Text


def kb_sender_buttons() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text=Text.SEND_YES.value)
    kb.button(text=Text.SEND_NO.value)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
