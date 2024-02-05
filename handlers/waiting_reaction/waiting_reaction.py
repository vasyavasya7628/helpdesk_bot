from aiogram import Router, F
from aiogram.types import Message

from keyboards.waiting_reaction.kb_waiting_reaction import kb_waiting_reaction
from data.db_methods import get_orders_waiting
from res.resources import Text

waiting_reaction_router = Router()


@waiting_reaction_router.message(F.text == Text.ACTIVE_ORDERS.value)
async def waiting_reaction(message: Message):
    order_list = get_orders_waiting()
    await message.answer(
        str(order_list),
        disable_web_page_preview=True,
        reply_markup=kb_waiting_reaction()
    )
