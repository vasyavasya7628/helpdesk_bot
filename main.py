import asyncio
import logging

from aiogram import Bot, Dispatcher

import res.resources as text
from handlers import start, exceptions, districts, register, reg_success


# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=text.bot_token())
    dp = Dispatcher()
    dp.include_routers(districts.districts_router,
                       start.start_router,
                       register.register_router,
                       reg_success.reg_success_router,
                       exceptions.exceptions_router
                       )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
