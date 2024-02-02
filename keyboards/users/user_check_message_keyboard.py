from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from res.resources import Text


def kb_message_correct() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text=Text.SEND_MESSAGE_TO_IT.value)
    kb.button(text=Text.DONT_SEND_NOT_SURE.value)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
