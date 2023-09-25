from aiogram import Router, F
from aiogram.types import Message

from res import resources as resources

exceptions_router = Router()


@exceptions_router.message(F.text)
async def message_with_text(message: Message):
    await message.answer(resources.text_incorrect_text())


@exceptions_router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer(resources.text_incorrect_image())


@exceptions_router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer(resources.text_incorrect_gif())
