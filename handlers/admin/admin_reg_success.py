from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.admin.admin_fsm import AdminFSM
from keyboards.admin.adm_success_keyboard import get_kb_reg_success
from data.db_methods import insert_user, delete_admin
from res.resources import Text

admin_reg_success_router = Router()


def list_item_equal(message):
    districts = Text.GET_DISTRICTS.value
    for i in range(len(districts)):
        if message == districts[i].lower():
            return message


def get_district_id(emoji, message_text):
    districts = Text.GET_DISTRICTS.value
    for i in range(len(districts)):
        if message_text.lower() == emoji + districts[i].lower():
            return districts[i + 1]


@admin_reg_success_router.message(AdminFSM.admin_reg_success)
async def adm_reg_success(message: Message, state: FSMContext):
    await state.clear()
    await delete_admin(message.from_user.id)
    await insert_user(get_district_id("➡", message.text),
                      message.from_user.id,
                      message.from_user.username,
                      message.from_user.first_name,
                      message.from_user.last_name)

    await message.answer(
        Text.END_REGISTER_FOR_ADMINS.value,
        reply_markup=get_kb_reg_success()
    )
