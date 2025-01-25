import os
from dotenv import load_dotenv
from pathlib import Path
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji

from datetime import datetime

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
dp['bot_reated'] = datetime.now().strftime('%H:%M:%S')
################################################


@dp.message(Command('add_to_list'))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer(f'added number 7 to list')
    await message.answer(f'{mylist}')

@dp.message(Command('show_list'))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f'{mylist}')


@dp.message(Command('dice'))
async def cmd_dice(message: types.Message, bot: Bot):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@dp.message(Command('test1'))
async def cmd_test1(message: types.Message):
    await message.answer('test1')


@dp.message(Command('test2'))
async def cmd_test2(message: types.Message):
    await message.reply('test2')


################################################
# Main entry point
async def main():
    await dp.start_polling(bot, mylist=[1, 2, 3])


if __name__ == "__main__":
    asyncio.run(main())
