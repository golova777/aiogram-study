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

# different types of link preview
@dp.message(Command('links'))
async def cmd_links(message: types.Message):
    links_text  = (
        'https://google.com\n'
        'https://ya.ru\n'
        'https://github.com\n'
        'https://stackoverflow.com\n'
        'https://t.me/telegram\n'
    )
    # No preview at all
    preview_options_1 = LinkPreviewOptions(is_disabled=True)

    # Small preview
    preview_options_2 = LinkPreviewOptions(
        url='https://github.com',
        prefer_small_media=True,
    )

    # Large preview
    preview_options_3 = LinkPreviewOptions(
        url='https://stackoverflow.com',
        prefer_large_media=True,
    )

    # Combined preview
    preview_options_4 = LinkPreviewOptions(
        url='https://stackoverflow.com',
        prefer_small_media=True,
        show_above_text=True,

    )

    preview_options_5 = LinkPreviewOptions(
        url="https://t.me/telegram"
    )

    await message.answer(
        links_text,
        link_preview_options=preview_options_5
    )





################################################
# Main entry point
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
