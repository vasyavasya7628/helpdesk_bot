from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.users.user_districts_kb import kb_user_districts
from keyboards.users.user_fsm import UserFSM
from res.resources import Text

user_district_router = Router()


@user_district_router.message(F.text == Text.WRITE_TO_IT.value)
async def usr_select_district(message: Message, state: FSMContext):
    await state.set_state(UserFSM.user_send_message_state)
    await message.answer(
        Text.USER_CHOOSE_DISTRICT.value,
        reply_markup=kb_user_districts()
    )
