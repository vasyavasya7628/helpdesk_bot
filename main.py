import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

import res.resources as text
from admin.handlers import admin_district
from handlers import start, exceptions_catcher
from user.handlers import user_district


# Запуск бота
async def main():
    bot = Bot(token=text.bot_token())
    dp = Dispatcher()
    dp.include_routers(start.start_router,
                       user_district.user_district_router,
                       admin_district.admin_districts_router,
                       exceptions_catcher.exceptions_router
                       )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
