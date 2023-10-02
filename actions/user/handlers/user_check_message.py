from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.user.keyboard.user_check_message_keyboard import kb_message_correct
from actions.user.user_fsm import UserFSM
from res.resources import text_message_correct

user_check_message_router = Router()


@user_check_message_router.message(UserFSM.user_check_message)
async def cmd_check_message(message: Message, state: FSMContext):
    await message.answer(
        text_message_correct(),
        reply_markup=kb_message_correct()
    )
    if message.text == "Да, отправить сообщение об ошибке специалистам":
        await state.set_state(UserFSM.user_message_sed_success)
    elif message.text == "Я не уверен(а), хочу изменить сообщение.":
        await state.set_state(UserFSM.user_send_message_state)
