import os
import re
from dotenv import load_dotenv
from pathlib import Path
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram import html
from aiogram.utils.formatting import Text, Bold
from datetime import datetime
from aiogram.types import LinkPreviewOptions

################################################
# Logging
logging.basicConfig(level=logging.INFO)
################################################

################################################
# Load .env
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
BOT_TOKEN = os.getenv('BOT_TOKEN')
################################################

################################################
# Init bot
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


################################################


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Well, hi!')


################################################
# Main entry point
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
