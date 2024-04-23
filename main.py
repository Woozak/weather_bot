import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config.config import Config, load_config


async def main():

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
