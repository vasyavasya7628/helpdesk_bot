from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.start_keyboard import get_kb_start

start_router = Router()


@start_router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Что нужно смертный:",
        reply_markup=get_kb_start()
    )


@start_router.message(F.text.lower() == "меню")  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Что нужно смертный:",
        reply_markup=get_kb_start()
    )
