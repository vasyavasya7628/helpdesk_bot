from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def kb_my_orders(admin_id, order_number) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Закрыть++", callback_data=str(admin_id))
    kb.button(text="Отложить--", callback_data=str(order_number))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
