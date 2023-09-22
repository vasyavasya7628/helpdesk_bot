from aiogram import Router, F
from aiogram.types import Message

import res.resources as text
from db_metods.table_user_id import insert_user
from keyboards.reg_success_keyboard import get_kb_reg_success

reg_success_router = Router()


def list_item_equal(message):
    districts = text.get_districts()
    for i in range(len(districts)):
        if message == districts[i].lower():
            return message


def get_district_id(message_text):
    districts = text.get_districts()
    for i in range(len(districts)):
        if message_text.lower() == districts[i].lower():
            return districts[i + 1]


@reg_success_router.message(F.text.lower() == list_item_equal(F.text.lower()))
async def cmd_select_district_reg(message: Message):
    insert_user(get_district_id(message.text), message.from_user.id)
    await message.answer(
        f"{message.text}",
        reply_markup=get_kb_reg_success()
    )
