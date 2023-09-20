import asyncio
import logging
import res.resources as text
from aiogram import Bot, Dispatcher
from handlers import start, exceptions_handling


# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=text.bot_token())
    dp = Dispatcher()

    dp.include_routers(start.router,
                       exceptions_handling.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
