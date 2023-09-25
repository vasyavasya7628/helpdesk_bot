from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import res.resources as res
from user.handlers.user_district import user_district_router
from user.keyboard.user_success_message_keyboard import get_kb_return
from user.user_states import UserFSM


@user_district_router.message(UserFSM.success_message)
async def cmd_return_to_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        res.order_send(),
        reply_markup=get_kb_return()
    )
