from aiogram.types import Message
from commands.commands import set_my_commands
from aiogram import Bot
async def start(message: Message, bot: Bot):
    await set_my_commands(bot)
    await message.answer('привет просто отправь мне видео\nи я отправлю тебе его id')
#hi
async def lose(message: Message):
    if message.content_type != 'video':
        await message.answer('Вы отправили не видео')
async def get_id(message: Message):
    await message.reply(f'вот id этого видео {message.video.file_id}')