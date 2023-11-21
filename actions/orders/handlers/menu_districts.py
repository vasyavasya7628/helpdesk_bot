from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from actions.orders.handlers.fsm_show_distrcts import DistrictsFSM
from actions.orders.keyboards.menu_district_keyboard import kb_menu_districts
from res.resources import order_list, text_orders

menu_district_router = Router()


@menu_district_router.message(F.text == order_list())
async def select_district(message: Message, state: FSMContext):
    await message.answer(
        text_orders(),
        reply_markup=kb_menu_districts()
    )
