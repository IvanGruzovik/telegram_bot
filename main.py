from aiogram import Dispatcher, Bot, F
import asyncio
from aiogram.filters import Command
from handlers.handlers import lose, get_id, start
token = '6875165306:AAGFx2BnTzSEtpUv3zYjh_e344UP6QAImd8'
bot = Bot(token=token)
dp = Dispatcher()
dp.message.register(start, Command('start'))
dp.message.register(lose, F.text | F.photo | F.sticker | F.file)
dp.message.register(get_id, F.video)
async def start():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(start())
