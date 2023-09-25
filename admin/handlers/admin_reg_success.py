from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import res.resources as text
from admin.admin_fsm.admin_states import AdminFSM
from admin.handlers.admin_district import admin_districts_router
from db_metods.table_user_id import insert_user
from keyboards.reg_success_keyboard import get_kb_reg_success


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


@admin_districts_router.message(AdminFSM.reg_success)
async def cmd_select_district_reg(message: Message, state: FSMContext):
    insert_user(get_district_id(message.text), message.from_user.id)
    await state.clear()
    await message.answer(
        f"{message.text}",
        reply_markup=get_kb_reg_success()
    )
