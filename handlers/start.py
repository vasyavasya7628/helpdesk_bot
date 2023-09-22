from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import res.resources as res
from keyboards.start_keyboard import get_kb_start

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        res.text_greetings(),
        reply_markup=get_kb_start()
    )


@start_router.message(
    F.text.lower() == "меню".lower())
async def cmd_start(message: Message):
    await message.answer(
        res.text_greetings(),
        reply_markup=get_kb_start()
    )


@start_router.message(F.text.lower() == res.text_register_complete().lower())
async def cmd_start(message: Message):
    await message.answer(
        res.text_greetings(),
        reply_markup=get_kb_start()
    )
