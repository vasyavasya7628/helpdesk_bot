from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.handlers.admin.admin_fsm import AdminFSM
from actions.keyboards.admin.adm_districts_kb import adm_districts_kb
from res.resources import Text

admin_districts_router = Router()
admin_change_district = Router()


@admin_districts_router.message(F.text.lower() == Text.ADMIN_LOGIN.value.lower())
async def admin_select_district(message: Message, state: FSMContext):
    await state.set_state(AdminFSM.admin_reg_success)
    await message.answer(
        Text.ADMIN_CHOOSE_DISTRICT.value,
        reply_markup=adm_districts_kb()
    )
