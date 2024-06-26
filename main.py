import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database.status_manager import manage_my_orders_router
from handlers.admin.admin_district import admin_districts_router
from handlers.admin.admin_reg_success import admin_reg_success_router
from handlers.admin.order_status import order_status_router_yes, order_status_router_no
from handlers.menu.exceptions_catcher import exceptions_router
from handlers.menu.start import start_router
from handlers.my_orders.my_orders import my_orders_router
from handlers.order_list.show_all_orders import order_info_router
from handlers.user.check_window import window_router
from handlers.user.success_message import user_success_router
from handlers.waiting_reaction.waiting_reaction import waiting_reaction_router


def get_bot():
    return


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start_router,
                       admin_districts_router,
                       admin_reg_success_router,
                       order_status_router_yes,
                       order_status_router_no,
                       manage_my_orders_router,
                       waiting_reaction_router,
                       window_router,
                       my_orders_router,
                       user_success_router,
                       order_info_router,
                       exceptions_router
                       )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    is_webhook_set = bot.get_webhook_info() is not None
    logging.info(is_webhook_set)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
