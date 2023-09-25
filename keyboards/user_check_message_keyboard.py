from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_kb_message_correct() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да, отправить сообщение специалисту")
    kb.button(text="Я не уверен(а), хочу изменить сообщение.")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
