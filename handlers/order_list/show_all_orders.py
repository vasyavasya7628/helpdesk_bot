from aiogram import Router, F
from aiogram.types import Message

from database.db_methods import get_order_info
from keyboards.orders.menu_district_keyboard import kb_menu_districts
from res.resources import Text


def generate_table_output(result):
    formatted_message = f"Список заявок:\n"
    for i in range(len(result)):
        message = ("______________________________\n"
                   f"📋 Номер заявки: {result[i][2]} \n"
                   f"От кого: {result[i][5]}\n"
                   f"Исполнитель: {none_check(result[i][6])} \n")
        message += f"   - Сообщение: {result[i][3]}\n"
        message += f"   - Время: {result[i][7]}\n"
        message += f"   - Статус: {result[i][10]}\n"
        formatted_message += message
    return formatted_message


def none_check(text):
    if text is None:
        return "\n"
    else:
        return text


order_info_router = Router()


@order_info_router.message(F.text == Text.ORDER_LIST.value)
async def show_db_orders(message: Message):
    result = await get_order_info()
    table_view = generate_table_output(result)
    while table_view:
        part, table_view = table_view[:4096], table_view[4096:]
        if part:
            await message.answer(
                part,
                disable_web_page_preview=True,
                reply_markup=kb_menu_districts()
            )
