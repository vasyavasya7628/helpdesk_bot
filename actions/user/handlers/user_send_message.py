from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, Message

from actions.user.user_fsm import UserFSM
from res.resources import describe_your_problem

user_send_message_router = Router()


# F.text.regexp(r'✅')
@user_send_message_router.message(UserFSM.user_send_message_state)
async def usr_send_message(message: Message, state: FSMContext):
    await state.set_state(UserFSM.user_check_message)
    await message.answer(
        describe_your_problem(),
        reply_markup=ReplyKeyboardRemove()
    )
