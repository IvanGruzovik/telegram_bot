from aiogram.types import BotCommand
from aiogram.types import BotCommandScopeDefault
from aiogram import Bot
#hi
async def set_my_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='начать'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())