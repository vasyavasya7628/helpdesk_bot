import logging

from aiogram import Router, F, Bot
from aiogram.types import Message

from db_metods.table_user_id import select_admins_same_district, check_none_string, add_worker_db
from keyboards.start_keyboard import get_kb_start
from res.resources import bot_token

order_status_router_yes = Router()
order_status_router_no = Router()





@order_status_router_yes.message(F.text == 'Да✅')
async def notify_admins_order_status(message: Message):
    bot = Bot(token=bot_token(), parse_mode="HTML")
    order_number = "121231421"
    #get_order_number_from_db()
    logging.info(str(message.text))
    other_admins_id = select_admins_same_district(message.from_user.id)
    add_worker_db(message.from_user.username, order_number)
    for i in range(len(other_admins_id)):
        if other_admins_id[i] is not message.from_user.id:
            await bot.send_message(other_admins_id[i],
                                   f"Заявку № {check_none_string(order_number)} \n Принял: " +
                                   f"{message.text}" +
                                   f"{check_none_string(message.from_user.first_name)}" +
                                   f"{check_none_string(message.from_user.last_name)} " +
                                   f"https://t.me/{check_none_string(message.from_user.username)}",
                                   reply_markup=get_kb_start())
    await bot.session.close()
    await message.answer("Главное меню",
                         reply_markup=get_kb_start())


@order_status_router_no.message(F.text == 'Нет❌')
async def return_to_main(message: Message):
    await message.answer("Главное меню",
                         reply_markup=get_kb_start())
