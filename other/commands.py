from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='restart',
            description='Перезагрузка'
        )
    ]
    await bot.set_my_commands(commands)