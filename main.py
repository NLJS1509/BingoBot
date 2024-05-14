from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram.client.bot import DefaultBotProperties
import asyncio
import logging
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(config.TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


async def main():
    from handlers import dp
    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())