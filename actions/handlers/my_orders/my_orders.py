from aiogram import F, Router
from aiogram.types import Message

from actions.keyboards.my_orders.my_orders_kb import get_my_orders
from actions.keyboards.orders.menu_district_keyboard import kb_menu_districts
from res.resources import Text

my_orders_router = Router()


@my_orders_router.message(F.text == Text.MY_ORDERS.value.lower())
async def select_district(message: Message):
    await message.answer(
        Text.ORDERS.value,
        reply_markup=get_my_orders()
    )
