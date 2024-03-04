import logging
import random
import time

from aiogram import Router, Bot
from aiogram.exceptions import TelegramForbiddenError
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from database.db_methods import check_none_string, add_order_info, store_order_number, get_admins
from handlers.user.user_fsm import UserFSM
from keyboards.users.kb_sender import kb_sender_buttons
from keyboards.users.user_success_message_keyboard import get_kb_return
from res.resources import Text

user_success_router = Router()


@user_success_router.message(UserFSM.success_message)
async def user_success_message(message: Message, state: FSMContext, bot: Bot):
    logging.info("Я в state UserFSM.success_message")
    order_number = generate_random_number()
    data_time = get_time()
    window_number = await state.get_data()
    window_number.setdefault('_window_', 'такого окна нет')
    await store_order_number(order_number)
    await add_order_info(order_number,
                         check_none_string(f"\n Окно номер: {window_number.get('window')}\n"
                                           f"{message.text}"),
                         f"{check_telegram_profile_link(message)}",
                         data_time)
    admin_list = await get_admins()
    for i in range(len(admin_list)):
        try:
            await bot.send_message(admin_list[i], f"Заявка №{generate_random_number()}: \n"
                                                  f"Окно номер: {window_number.get('window')}\n"
                                   + f"{message.text}"
                                   + f"\n От специалиста: {check_telegram_profile_link(message)}",
                                   disable_web_page_preview=True,
                                   reply_markup=kb_sender_buttons())
        except TelegramForbiddenError:
            logging.info(f"{admin_list[i]} заблокировал бота")
    await state.clear()
    await message.answer(
        Text.ORDER_SEND.value,
        reply_markup=get_kb_return()
    )


def check_telegram_profile_link(message):
    try:
        if message.from_user.username is not None:
            return check_none_string(f"https://t.me/{message.from_user.username}")
        else:
            return (f"{check_none_string(message.from_user.last_name)} "
                    f"{check_none_string(message.from_user.first_name)}")
    except AttributeError:
        return (f"{check_none_string(message.from_user.last_name)} "
                f"{check_none_string(message.from_user.first_name)}")


def generate_random_number():
    first_digit = 1
    other_digits = [random.randint(0, 9) for _ in range(7)]
    random_number = int(''.join(map(str, [first_digit] + other_digits)))
    return random_number


def get_time():
    named_tuple = time.localtime()
    time_string = time.strftime("%d.%m.%Y, %H:%M", named_tuple)
    return time_string
