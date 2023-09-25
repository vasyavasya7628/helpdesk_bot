from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import res.resources as res
from admin.admin_fsm.admin_states import AdminFSM
from keyboards.districts_keyboard import get_kb_districts

admin_districts_router = Router()


@admin_districts_router.message(F.text.lower() == res.text_admin_login().lower())
async def cmd_select_district(message: Message, state: FSMContext):
    await state.set_state(AdminFSM.choose_district)
    await message.answer(
        res.text_admin_choose_district(),
        reply_markup=get_kb_districts()
    )
