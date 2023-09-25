from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import res.resources as res
from admin.admin_fsm.admin_states import AdminFSM
from admin.handlers.admin_district import admin_districts_router
from keyboards.register_keyboard import get_kb_register


@admin_districts_router.message(AdminFSM.choose_district)
async def cmd_select_district_reg(message: Message, state: FSMContext):
    await state.set_state(AdminFSM.reg_success)
    await message.answer(
        res.text_chose_district_from_list(),
        reply_markup=get_kb_register()
    )
