import os
from dotenv import load_dotenv
from pathlib import Path
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandObject
from aiogram import html
from aiogram.utils.formatting import Text, Bold
from datetime import datetime

################################################
# Documentation
# https://mastergroosha.github.io/aiogram-3-guide/messages/
################################################

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
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ),
)
dp = Dispatcher()


################################################

# commands with custom prefix
# @dp.message(Command('settimer', prefix='$'))
# Can set several chars as prefix
# @dp.message(Command('settimer', prefix='%!$'))

@dp.message(Command('settimer'))
async def set_timer(
        message: types.Message,
        command: CommandObject,
):
    if command.args is None:
        await message.answer(
            'Error: no arguments provided.'
        )
        return
    # there are arguments, trying to split them by the first space
    try:
        delay_time, text_to_send = command.args.split(' ', maxsplit=1)
    except Exception:
        # wrong parameters
        await message.answer(
            'Error: wrong arguments provided. \n/settimer <time> <message>',
            parse_mode=None,
        )
        return
    # everything is OK!
    await message.answer(
        f'Timer was set\n'
        f'Time: {delay_time}\n'
        f'Text {text_to_send}\n'
    )


@dp.message(F.text)
async def extract_data(message: types.Message):
    ###############################################
    # extract every URL/HASHTAG/EMAIL.... entitie
    ###############################################
    data = {
        "url": [],
        "email": [],
        "code": [],
    }
    entities = message.entities or []
    for item in entities:
        if item.type in data.keys():
            data[item.type].append(item.extract_from(message.text))

    await message.answer(
        f'That\'s what i\'ve found:\n'
        f'URL: {data["url"]}\n'
        f'EMAIL: {data["email"]}\n'
        f'CODE: {data["code"]}\n'

    )


# @dp.message(F.text)
# async def extract_data(message: types.Message):
#     entities = message.entities or []
#     print(entities)
#     await message.answer(
#         f'You\'ve just send me {message.text}', 
#     )


@dp.message(F.text)
async def echo_with_time(message: types.Message):
    time_now = datetime.now().strftime('%H:%M:%S')
    added_text = html.bold(f'created at {time_now}')
    await message.answer(
        f'{message.html_text}\n\n{added_text}',
    )


@dp.message(Command('hello'))
async def cmd_hello(message: types.Message):
    content = Text(
        'Hello, ',
        Bold(message.text),
    )
    await message.answer(
        **content.as_kwargs(),
    )


# @dp.message(Command('hello'))
# async def cmd_hello(message: types.Message):
#     await message.answer(
#         f'Hello, {html.quote(html.bold(message.text))}',
#         parse_mode=ParseMode.HTML,
#     )


# @dp.message(Command('hello'))
# async def cmd_hello(message: types.Message):
#     await message.answer(
#         f'Hello, <b>{message.text}</b>',
#         parse_mode=ParseMode.HTML,
#     )


@dp.message(F.text, Command('test'))
async def any_message(message: types.Message):
    await message.answer(
        f'hello <b>world</b>! <u>{message.text}</u>',
    )
    await message.answer(
        f'hello <b>world</b> {message.text}',
        parse_mode=None,
    )


@dp.message(F.text)
async def echo_message(message: types.Message):
    await message.answer(f'You\'ve just send me {message.text}')


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Well, hi!')


################################################
# Main entry point
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
