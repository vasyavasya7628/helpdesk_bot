import logging

from aiogram import Router, F, Bot
from aiogram.types import Message

from actions.keyboards.menu.start_keyboard import get_kb_start
from data.db_methods import select_admins_same_district, check_none_string, add_worker, get_order_number, \
    change_order_status
from res.resources import Text, OrderStatus

order_status_router_yes = Router()
order_status_router_no = Router()


@order_status_router_yes.message(F.text == Text.SEND_YES.value)
async def notify_admins_order_status(message: Message, bot: Bot):
    order_number = await get_order_number()
    logging.info(f"НОМЕР ЗАЯВКИ{order_number}")
    await change_order_status(order_number, OrderStatus.IN_PROCESS.value)
    logging.info(str(message.text))
    other_admins_id = await select_admins_same_district(message.from_user.id)
    await add_worker(f"https://t.me/{check_none_string(message.from_user.username)}",
                     order_number)
    for i in range(len(other_admins_id)):
        if other_admins_id[i] is not message.from_user.id:
            await bot.send_message(other_admins_id[i],
                                   f"Заявку № {check_none_string(order_number)} \nПринял: " +
                                   f"https://t.me/{check_none_string(message.from_user.username)}",
                                   disable_web_page_preview=True,
                                   reply_markup=get_kb_start())
    await bot.session.close()
    await message.answer("Главное меню",
                         reply_markup=get_kb_start())


@order_status_router_no.message(F.text == 'Нет❌')
async def return_to_main(message: Message):
    await message.answer("Главное меню",
                         reply_markup=get_kb_start())
