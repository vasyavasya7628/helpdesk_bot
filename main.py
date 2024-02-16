import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.session_middleware import DbSessionMiddleware
from handlers.admin.admin_district import admin_districts_router
from handlers.admin.admin_reg_success import admin_reg_success_router
from handlers.admin.order_status import order_status_router_yes, order_status_router_no
from handlers.menu.exceptions_catcher import exceptions_router
from handlers.menu.start import start_router
from handlers.my_orders.manage_my_orders import manage_my_orders_router
from handlers.my_orders.my_orders import my_orders_router
from handlers.order_list.menu_districts import menu_district_router
from handlers.order_list.show_all_orders import order_info_router
from handlers.user.user_district import user_district_router
from handlers.user.user_send_message import user_send_message_router
from handlers.user.user_success_message import user_success_router
from handlers.waiting_reaction.waiting_reaction import waiting_reaction_router
from res.secret import bot_token, DatabaseOp as conn_string


def get_bot():
    return


async def main():
    engine = create_async_engine(url=conn_string.value, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    bot = Bot(token=bot_token(), parse_mode="HTML")
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    dp.include_routers(start_router,
                       admin_districts_router,
                       admin_reg_success_router,
                       order_status_router_yes,
                       order_status_router_no,
                       manage_my_orders_router,
                       user_district_router,
                       waiting_reaction_router,
                       user_send_message_router,
                       my_orders_router,
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
