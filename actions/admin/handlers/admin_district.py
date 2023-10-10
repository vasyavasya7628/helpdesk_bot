from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.admin.admin_fsm import AdminFSM
from actions.admin.keyboards.adm_districts_kb import adm_districts_kb
from res.resources import text_admin_choose_district, text_admin_login

admin_districts_router = Router()
admin_change_district = Router()


@admin_districts_router.message(F.text.lower() == text_admin_login().lower())
async def admin_select_district(message: Message, state: FSMContext):
    await state.set_state(AdminFSM.admin_reg_success)
    await message.answer(
        text_admin_choose_district(),
        reply_markup=adm_districts_kb()
    )
