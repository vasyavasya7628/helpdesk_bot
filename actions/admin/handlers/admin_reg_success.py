from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.admin.admin_fsm import AdminFSM
from actions.admin.keyboards.adm_success_keyboard import get_kb_reg_success
from db_metods.table_user_id import insert_user, delete_admin_from_db
from res.resources import text_end_register_for_admins, get_districts

admin_reg_success_router = Router()


def list_item_equal(message):
    districts = get_districts()
    for i in range(len(districts)):
        if message == districts[i].lower():
            return message


def get_district_id(message_text):
    districts = get_districts()
    for i in range(len(districts)):
        if message_text.lower() == "➡" + districts[i].lower():
            return districts[i + 1]


@admin_reg_success_router.message(AdminFSM.admin_reg_success)
async def adm_reg_success(message: Message, state: FSMContext):
    await state.clear()
    delete_admin_from_db(message.from_user.id)
    insert_user(get_district_id(message.text),
                message.from_user.id,
                message.from_user.username,
                message.from_user.first_name,
                message.from_user.last_name)
    await message.answer(
        text_end_register_for_admins(),
        reply_markup=get_kb_reg_success()
    )
