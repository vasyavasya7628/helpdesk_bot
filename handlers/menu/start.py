from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from database.db_methods import check_role
from keyboards.menu.start_keyboard import get_kb_start
from res.resources import Text

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    role = await check_role(message.from_user.id)
    await message.answer(
        Text.GREETINGS.value,
        reply_markup=get_kb_start(role)
    )


@start_router.message(F.text == Text.RETURN_TO_MAIN_MENU.value)
async def cmd_start(message: Message):
    role = await check_role(message.from_user.id)
    await message.answer(
        Text.GREETINGS.value,
        reply_markup=get_kb_start(role)
    )


@start_router.message(
    F.text.lower() == Text.MENU.value.lower())
async def cmd_start(message: Message):
    role = await check_role(message.from_user.id)
    await message.answer(
        Text.GREETINGS.value,
        reply_markup=get_kb_start(role)
    )


@start_router.message(F.text.lower() == Text.REGISTER_COMPLETE.value.lower())
async def cmd_start(message: Message):
    await message.answer(
        Text.GREETINGS.value,
        reply_markup=get_kb_start()
    )
