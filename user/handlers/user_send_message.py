from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

import res.resources as res
from user.handlers.user_district import user_district_router
from user.user_states import UserFSM


@user_district_router.message(UserFSM.send_message)
async def cmd_send_message(message: Message, state: FSMContext):
    await state.set_state(UserFSM.check_message)
    await message.answer(
        res.describe_your_problem(),
        reply_markup=ReplyKeyboardRemove()
    )
