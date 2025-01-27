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

""" Существует одна команда в Telegram, у которой есть чуть больше возможностей. Это /start. 
Дело в том, что можно сформировать ссылку вида t.me/bot?start=xxx и пре переходе по такой ссылке 
пользователю покажут кнопку «Начать», при нажатии которой бот получит сообщение /start xxx. Т.е. 
в ссылке зашивается некий дополнительный параметр, не требующий ручного ввода. Это называется 
диплинк (не путать с дикпиком) и может использоваться для кучи разных вещей: шорткаты для активации 
различных команд, реферальная система, быстрая конфигурация бота и т.д.
"""

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

# https://t.me/aiogram_course_tar_bot?start=help
@dp.message(Command('help'))
@dp.message(CommandStart(
    deep_link=True,
    magic=F.args == 'help',
))
async def cmd_start_help(message: types.Message):
    await message.answer('that is a help message')


# providing custom parameter while starting bot
# https://t.me/aiogram_course_tar_bot?start=book_565
@dp.message(CommandStart(
    deep_link=True,
    magic=F.args.regexp(re.compile(r'book_(\d+)'))
))
async def cmd_start_book(
        message: types.Message,
        command: CommandObject,
):
    book_number = command.args.split("_")[1]
    print(command.args)
    await message.answer(f'sending a book #{book_number}')


################################################
# Main entry point
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
