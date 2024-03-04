import asyncio
import logging
import sys

import aiosqlite

from data.db_methods import get_db_path


async def test():
    try:
        async with aiosqlite.connect(get_db_path()) as conn:
            cursor = await conn.execute("SELECT user_id FROM users;")
            data = await cursor.fetchall()
            logging.info(f"{[item[0] for item in data]}")
            return [item[0] for item in data]
    except aiosqlite.Error as error:
        logging.info(f"[ERROR] in function add_order_info: {error}")


async def main():
    await test()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
