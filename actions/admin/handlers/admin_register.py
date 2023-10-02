from aiogram import F, Router
from aiogram.types import Message

from actions.admin.keyboards.admin_register_kb import admin_register_kb
from res.resources import text_admin_choose_district

admin_register_router = Router()


@admin_register_router.message(F.text.regexp(r'➡'))
async def adm_select_district_reg(message: Message):
    await message.answer(
        text_admin_choose_district(),
        reply_markup=admin_register_kb()
    )
