import logging

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import res.resources as res
from keyboards.districts_keyboard import get_kb_districts
from user.user_states import UserFSM

user_district_router = Router()


@user_district_router.message(F.text.lower() == res.text_write_to_it().lower())
async def cmd_select_district(message: Message, state: FSMContext):
    logging.info("Устанавливаем состояние UserFSM.send_message")
    await state.set_state(UserFSM.send_message)
    reply_message = message.reply_to_message
    await message.answer(
        res.text_user_choose_district(),
        reply_markup=get_kb_districts()
    )
