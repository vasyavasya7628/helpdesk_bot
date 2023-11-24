import asyncio

from aiogram import Router, F
from aiogram.types import Message

from actions.handlers.admin.admin_reg_success import get_district_id
from actions.keyboards.orders.menu_district_keyboard import kb_menu_districts
from data.db_methods import get_order_info

order_info_router = Router()


@order_info_router.message(F.text.startswith('💼'))
async def show_db_orders(message: Message):
    district_id = get_district_id("💼", message.text)
    result = await asyncio.gather(get_order_info(district_id))
    table_view = generate_table_output(result)
    while table_view:
        part, table_view = table_view[:4096], table_view[4096:]
        if part:
            await message.answer(
                part,
                disable_web_page_preview=True,
                reply_markup=kb_menu_districts()
            )


def generate_table_output(result):
    formatted_message = f"Список заявок:\n"

    # Перебираем данные и добавляем их в форматированный текст
    for entry in result:
        message = ("______________________________\n"
                   f"Номер заявки: {entry[0]} \n"
                   f"От кого: {entry[1]}\n"
                   f"Исполнитель: {none_check(entry[2])} \n")
        message += f"   - Сообщение: {entry[2]}\n"
        message += f"   - Время: {entry[0]}\n"
        formatted_message += message
    return formatted_message


def none_check(text):
    if text is None:
        return "Нет \n"
    else:
        return text
