from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.keyboards.orders.menu_district_keyboard import kb_menu_districts
from res.resources import text_orders, text_my_orders

my_orders_router = Router()


@my_orders_router.message(F.text == text_my_orders())
async def select_district(message: Message):
    await message.answer(
        text_orders(),
        reply_markup=kb_menu_districts()
    )
