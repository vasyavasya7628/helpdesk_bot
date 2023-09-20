from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.start_keyboard import get_kb_start

router = Router()


@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Что нужно смертный:",
        reply_markup=get_kb_start()
    )


@router.message(F.text.lower() == "🏻‍💻 Написать в IT-Отдел")
async def answer_yes(message: Message):
    await message.answer(
        "Это здорово!",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == "Зарегистрироваться(Для администраторов")
async def answer_no(message: Message):
    await message.answer(
        "Жаль...",
        reply_markup=ReplyKeyboardRemove()
    )
