from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.user.keyboard.user_districts_kb import kb_user_districts
from actions.user.user_fsm import UserFSM
from res.resources import text_user_choose_district, text_write_to_it

user_district_router = Router()


@user_district_router.message(F.text == text_write_to_it())
async def usr_select_district(message: Message, state: FSMContext):
    await state.set_state(UserFSM.user_send_message_state)
    await message.answer(
        text_user_choose_district(),
        reply_markup=kb_user_districts()
    )
