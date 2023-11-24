import asyncio
import logging
import random
import time

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.keyboards.users.kb_sender import kb_sender_buttons
from actions.keyboards.users.user_fsm import UserFSM
from actions.keyboards.users.user_success_message_keyboard import get_kb_return
from data.db_methods import select_user_id, check_none_string, add_order_info, store_order_number
from res.resources import get_districts, text_order_send

user_success_router = Router()


@user_success_router.message(UserFSM.user_success_message)
async def user_success_message(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    order_number = generate_random_number()
    data_time = get_time()
    await asyncio.gather(
        store_order_number(order_number),
        add_order_info(find_equal_district_id(data['choose_district']),
                       order_number,
                       check_none_string(message.text),
                       f"https://t.me/{check_none_string(message.from_user.username)}",
                       data_time)
    )
    admin_id = await find_user_id(data['choose_district'])
    for i in range(len(admin_id)):
        logging.info(f"user id = {admin_id[i]}")
        await bot.send_message(admin_id[i], f"Заявка №{generate_random_number()}: \n"
                               + f"{message.text}"
                               + f"\n От специалиста: https://t.me/{check_none_string(message.from_user.username)}",
                               disable_web_page_preview=True,
                               reply_markup=kb_sender_buttons())
    await state.clear()
    await message.answer(
        text_order_send(),
        reply_markup=get_kb_return()
    )
    await bot.session.close()


def find_user_id(chosen_district):
    district_id = find_equal_district_id(chosen_district)
    # возвращается список ид админов которые принадлежат выбранному ведомству
    return select_user_id(district_id)


def find_equal_district_id(chosen_district):
    list_district = get_districts()
    for i in range(len(list_district)):
        logging.info(f"ВЕДОМСТВО:{i + 1}")
        if f"✅{list_district[i]}" == chosen_district:
            logging.info(f"ИД ВЫБРАННОГО ВЕДОМСТВА:{list_district[i + 1]}")
            return list_district[i + 1]


def generate_random_number():
    first_digit = 1
    other_digits = [random.randint(0, 9) for _ in range(7)]
    random_number = int(''.join(map(str, [first_digit] + other_digits)))
    return random_number


def get_time():
    named_tuple = time.localtime()
    time_string = time.strftime("%d.%m.%Y, %H:%M", named_tuple)
    return time_string
