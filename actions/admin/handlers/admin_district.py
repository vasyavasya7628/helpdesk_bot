import logging

from aiogram import Router, F
from aiogram.types import Message

from actions.admin.keyboards.adm_districts_kb import adm_districts_kb
from res.resources import text_admin_choose_district, text_admin_login

admin_districts_router = Router()


@admin_districts_router.message(F.text.lower() == text_admin_login().lower())
async def adm_select_district(message: Message):
    logging.info(f"{F.text}")
    await message.answer(
        text_admin_choose_district(),
        reply_markup=adm_districts_kb()
    )
