from aiogram import Router, F
from aiogram.types import Message

import res.resources as text
from keyboards.register_keyboard import get_kb_register
import db_operations.db_methods
register_router = Router()


@register_router.message(F.text.lower() == text.text_admin_login().lower())
async def cmd_select_district_reg(message: Message):
    await message.answer(
        text.text_chose_district_from_list(),
        reply_markup=get_kb_register()
    )
