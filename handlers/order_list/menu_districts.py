from aiogram import F, Router
from aiogram.types import Message

from keyboards.orders.menu_district_keyboard import kb_menu_districts
from res.resources import Text

menu_district_router = Router()


@menu_district_router.message(F.text == Text.ORDER_LIST.value)
async def select_district(message: Message):
    await message.answer(
        Text.ORDERS.value,
        reply_markup=kb_menu_districts()
    )
