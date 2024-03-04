import logging

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.user.user_fsm import UserFSM
from keyboards.menu.start_keyboard import get_kb_start
from res.resources import Text

exit_to_menu_router = Router()


@exit_to_menu_router.message(F.text == Text.EXIT_TO_MENU.value)
async def exit_to_menu(message: Message, state: FSMContext):
    logging.info("Я ОТМЕНЯЮ ПРОБЛЕМУ")
    await state.set_state(UserFSM.cancel_message)
    await state.clear()
    await message.answer(text="Выход в меню", reply_markup=get_kb_start())
