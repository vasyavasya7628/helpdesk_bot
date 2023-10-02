from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.user.keyboard.user_success_message_keyboard import get_kb_return
from actions.user.user_fsm import UserFSM
from res.resources import order_send

user_return_to_menu_router = Router()


@user_return_to_menu_router.message(UserFSM.user_message_sed_success)
async def user_return_to_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        order_send(),
        reply_markup=get_kb_return()
    )
