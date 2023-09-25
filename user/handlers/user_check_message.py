from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import res.resources as res
from keyboards.user_check_message_keyboard import get_kb_message_correct
from user.handlers.user_district import user_district_router
from user.user_states import UserFSM


@user_district_router.message(UserFSM.check_message)
async def cmd_check_message(message: Message, state: FSMContext):
    await state.set_state(UserFSM.success_message)
    await message.answer(
        res.text_message_correct(),
        reply_markup=get_kb_message_correct()
    )
