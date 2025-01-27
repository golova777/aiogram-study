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
import pprint

################################################
# Logging
logging.basicConfig(level=logging.DEBUG)
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


# @dp.message(Command('test'))
# async def cmd_test(message: types.Message):
#     await message.answer_animation('CgACAgIAAxkBAAIBrGeV7GhM3klZUctn0GhU4hFGeMlUAAJtBQACr3PBSSLiYVVnGRSnNgQ')

@dp.message(F.video)
@dp.message(F.text)
@dp.message(F.photo)
@dp.message(F.animation)
async def echo_gif(message: types.Message):
    gifs = ['CgACAgIAAxkBAAIBrGeV7GhM3klZUctn0GhU4hFGeMlUAAJtBQACr3PBSSLiYVVnGRSnNgQ',]
    [await message.answer_animation(gif) for gif in gifs]




################################################
# Main entry point
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
