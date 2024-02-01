import logging

from aiogram import F, Router, Bot
from aiogram.types import Message

from actions.handlers.order_list.show_all_orders import none_check
from actions.keyboards.my_orders.kb_my_orders import kb_my_orders
from data.db_methods import sync_get_order_info
from res.resources import Text

my_orders_router = Router()


@my_orders_router.message(F.text == Text.MY_ORDERS.value)
async def show_orders(message: Message, bot: Bot):
    formatted_message = f"Список заявок:\n"
    order_list = sync_get_order_info(message.from_user.id)
    for i in range(len(order_list)):
        order_text = (f"Номер заявки: {order_list[i][2]} \n"
                      f"От кого: {order_list[i][5]}\n"
                      f"Исполнитель: {none_check(order_list[0][6])} \n")
        order_text += f"   - Сообщение: {order_list[i][3]}\n"
        order_text += f"   - Время: {order_list[i][7]}\n"
        order_text += f"   - Статус: {order_list[i][10]}\n"
        formatted_message += order_text
        await bot.send_message(chat_id=message.chat.id, text=order_text, disable_web_page_preview=True,
                               reply_markup=kb_my_orders(message.from_user.id, order_list[i][2]))
