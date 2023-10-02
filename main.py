import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from actions.admin.handlers.admin_district import admin_districts_router
from actions.admin.handlers.admin_reg_success import admin_reg_success_router
from actions.admin.handlers.admin_register import admin_register_router
from actions.user.handlers.user_check_message import user_check_message_router
from actions.user.handlers.user_district import user_district_router
from actions.user.handlers.user_send_message import user_send_message_router
from actions.user.handlers.user_success_message import user_return_to_menu_router
from handlers.exceptions_catcher import exceptions_router
from handlers.start import start_router
from res.resources import bot_token


# Запуск бота
async def main():
    bot = Bot(token=bot_token(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start_router,
                       admin_districts_router,
                       admin_reg_success_router,
                       admin_register_router,
                       user_district_router,
                       user_send_message_router,
                       user_check_message_router,
                       user_return_to_menu_router,
                       exceptions_router
                       )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
