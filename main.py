from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from buttons import insta, portfolio, responsibilities, adm_profile
import asyncio

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

@dp.message(CommandStart())
async def start_process(message: Message):
    await message.answer("Hi! It's LDLN bot. \nYou can push on menu button to see commands. \nTo get more info - /help")

@dp.message(Text(text='/help'))
async def help_process(message: Message):
    await message.answer(
'This bot was created by the LDLN team. \nWith it, you will be able to use our resources without any difficulty. \n\nIn addition, you can contact our administrator who will help you.\n\nIn the menu tab you can find shortcut commands\nAll commands available for use:\n/help\n/start\n/info\n/insta\n/portfolio\n/responsibilities\n/adm_profile\n/login (Only for admins team)')

@dp.message(Text(text='/info'))
async def help_process(message: Message):
    await message.answer('Our team name is LDLN.\nWe are working in copyraing and creating telegram bots.\n\nWe have 2 years of experience in this topic, a large number of positive reviews and completed work.\n\nBy this bot you can find all information about us and take contact with our administration')

@dp.message(Text(text='/adm_profile'))
async def help_process(message: Message):
    await message.answer('Link to our admin profile', reply_markup=adm_profile)

@dp.message(Text(text='/responsibilities'))
async def help_process(message: Message):
    await message.answer('Link to our responsibilities', reply_markup=responsibilities)

@dp.message(Text(text='/portfolio'))
async def help_process(message: Message):
    await message.answer('Link to our portfolio', reply_markup=portfolio)

@dp.message(Text(text='/insta'))
async def help_process(message: Message):
    await message.answer('Link to our instagram account', reply_markup=insta)


if __name__ == '__main__':
    dp.run_polling(bot)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())