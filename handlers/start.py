from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.start_keyboard import get_kb_start
from res.resources import text_return_to_main_menu, text_register_complete, text_greetings

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        text_greetings(),
        reply_markup=get_kb_start()
    )


@start_router.message(F.text == text_return_to_main_menu())
async def cmd_start(message: Message):
    await message.answer(
        text_greetings(),
        reply_markup=get_kb_start()
    )


@start_router.message(
    F.text.lower() == "меню".lower())
async def cmd_start(message: Message):
    await message.answer(
        text_greetings(),
        reply_markup=get_kb_start()
    )


@start_router.message(F.text.lower() == text_register_complete().lower())
async def cmd_start(message: Message):
    await message.answer(
        text_greetings(),
        reply_markup=get_kb_start()
    )
