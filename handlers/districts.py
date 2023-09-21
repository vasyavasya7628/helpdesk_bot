from aiogram import Router, F
from aiogram.types import Message

import res.resources as text
from keyboards.districts_keyboard import get_kb_districts

districts_router = Router()


@districts_router.message(F.text.lower() == text.text_write_to_it().lower())
async def cmd_select_district(message: Message):
    await message.answer(
        text.text_chose_district_from_list(),
        reply_markup=get_kb_districts()
    )
