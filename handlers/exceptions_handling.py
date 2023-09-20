from aiogram import Router, F
from aiogram.types import Message
from res import resources as resources
router = Router()


@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer(resources.text_incorrect_text())


@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer(resources.text_incorrect_image())


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer(resources.text_incorrect_gif())
