from aiogram import Router, F, Bot
from aiogram.types import Message
from numba import njit

from database.db_methods import order_info
from handlers.order_list.show_all_orders import none_check
from keyboards.waiting_reaction.kb_waiting_reaction import kb_waiting_reaction
from res.resources import Text

waiting_reaction_router = Router()


@njit(parallel=True)
@waiting_reaction_router.message(F.text == Text.ACTIVE_ORDERS.value)
async def show_waiting_orders(message: Message, bot: Bot):
    formatted_message = f"Список заявок:\n"
    order_list = await order_info(message.from_user.id)
    for i in range(len(order_list)):
        order_text = (f"Номер заявки: {order_list[i][2]} \n"
                      f"От кого: {order_list[i][5]}\n"
                      f"Исполнитель: {none_check(order_list[0][6])} \n")
        order_text += f"   - Сообщение: {order_list[i][3]}\n"
        order_text += f"   - Время: {order_list[i][7]}\n"
        order_text += f"   - Статус: {order_list[i][10]}\n"
        formatted_message += order_text
        await bot.send_message(chat_id=message.chat.id, text=order_text, disable_web_page_preview=True,
                               reply_markup=kb_waiting_reaction(message.from_user.id, order_list[i][2]))
