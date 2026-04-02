import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQuery

TOKEN = "YOUR_TOKEN_HERE

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.inline_query()
async def log_inline_query(inline_query: InlineQuery):
    print(f"User {inline_query.from_user.first_name} sent: {inline_query.query}")
    
    await inline_query.answer(results=[], cache_time=0)

async def main():
    print("Listening for inline queries...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass