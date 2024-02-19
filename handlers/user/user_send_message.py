import logging
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.users.user_fsm import UserFSM
from res.resources import Text

user_send_message_router = Router()


# выбирая ведомство, пользователь выбирает его id
@user_send_message_router.message(F.text == Text.WRITE_TO_IT.value)
async def user_send_message(message: Message, state: FSMContext):
    await state.set_data(data={"choose_district": message.text})
    await state.set_state(UserFSM.user_success_message)
    await message.answer(
        Text.DESCRIBE_YOUR_PROBLEM.value,
        reply_markup=ReplyKeyboardRemove()
    )
