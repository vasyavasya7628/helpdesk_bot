import logging

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

import res.resources as res
from user.handlers.user_district import user_district_router
from user.user_states import UserFSM


def text_equal_list_item(text):
    district_list = res.get_districts()
    for item in range(len(district_list)):
        if text == district_list[item]:
            return text
        else:
            return "false"


@user_district_router.message(UserFSM.send_message)
@user_district_router.message(F.text.lower() == text_equal_list_item(F.text.lower()))
async def cmd_send_message(message: Message, state: FSMContext):
    logging.info("Устанавливаем состояние UserFSM.check_message")
    await state.set_state(UserFSM.check_message)
    await message.answer(
        res.describe_your_problem(),
        reply_markup=ReplyKeyboardRemove()
    )
