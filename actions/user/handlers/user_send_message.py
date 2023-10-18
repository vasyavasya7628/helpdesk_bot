import logging

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from actions.user.user_fsm import UserFSM
from res.resources import text_describe_your_problem


user_send_message_router = Router()


# выбирая ведомство, пользователь выбирает его id


@user_send_message_router.message(UserFSM.user_send_message_state)
async def user_send_message(message: Message, state: FSMContext):
    logging.info(f"ВЫ ВЫБРАЛИ = {message.text}")
    await state.set_data(data={"choose_district": message.text})
    await state.set_state(UserFSM.user_success_message)
    await message.answer(
        text_describe_your_problem(),
        reply_markup=ReplyKeyboardRemove()
    )
