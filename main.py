import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from actions.handlers.admin.admin_district import admin_districts_router
from actions.handlers.admin.admin_reg_success import admin_reg_success_router
from actions.handlers.admin.order_status import order_status_router_yes, order_status_router_no
from actions.handlers.orders.db_orders import order_info_router
from actions.handlers.orders.menu_districts import menu_district_router
from actions.handlers.user.user_district import user_district_router
from actions.handlers.user.user_send_message import user_send_message_router
from actions.handlers.user.user_success_message import user_success_router
from actions.handlers.menu.exceptions_catcher import exceptions_router
from actions.handlers.menu.start import start_router
from res.resources import Text


# https://getemoji.com/
def get_bot():
    return


async def main():
    bot = Bot(token=Text.BOT_TOKEN.value, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(start_router,
                       admin_districts_router,
                       admin_reg_success_router,
                       order_status_router_yes,
                       order_status_router_no,
                       user_district_router,
                       user_send_message_router,
                       user_success_router,
                       menu_district_router,
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
