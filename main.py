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


# Создаем объекты кнопок
button_to_show_copywriting: KeyboardButton = KeyboardButton(text='Copywriting')
button_to_show_Tbots: KeyboardButton = KeyboardButton(text='Telegram bots')

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_to_show_copywriting], [button_to_show_Tbots]],
                                    resize_keyboard=True,
                                    one_time_keyboard=True)

@dp.message(CommandStart())
async def start_process(message: Message):
    await message.answer("Hi! It's LDLN bot. \nYou can push on menu button to see commands. \nTo get more info - /help")

@dp.message(Text(text='/help'))
async def help_process(message: Message):
    await message.answer(
'This bot was created by the LDLN team. \nWith it, you will be able to use our resources without any difficulty. \n\nIn addition, you can contact our administrator who will help you.\n\nIn the menu tab you can find shortcut commands\nAll commands available for use:\n/help\n/start\n/info\n/insta\n/portfolio\n/responsibilities\n/adm_profile\n/login (Only for admins team)\n/products')

@dp.message(Text(text='/info'))
async def help_process(message: Message):
    await message.answer('Our team name is LDLN.\nWe are working in copyraing and creating telegram bots.\n\nWe have 2 years of experience in this topic, a large number of positive reviews and completed work.\n\nBy this bot you can find all information about us and take contact with our administration')
    chat_id = message.from_user.id
    photo_url = 'https://sun9-20.userapi.com/impg/PNWUyscS_YFxpxZ39GYciw7ORDIp_5f2kQJZfw/bKFI5uwco9c.jpg?size=1024x1024&quality=95&sign=6d3a41795e2fcc3cf4f3711be5b33ac6&c_uniq_tag=n4ot2IgNONhy4kmc5BXi4ErKJDtTnpleY00prcTICr8&type=album'
    await bot.send_photo(chat_id, photo_url)

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


@dp.message(Text(text='/products'))
async def show_products(message: Message):
    await message.answer('Select the type of product you are interested in', reply_markup=keyboard)

@dp.message(Text(text='Copywriting'))
async def show_copywriting(message: Message):
    chat_id = message.from_user.id
    photo_url = 'https://sun9-18.userapi.com/impg/4BMie2By2D6UrTFJF2YxoT7uzsa0WpJdbtFO9g/LKXEhhA0wMw.jpg?size=924x733&quality=95&sign=cc4f4b1923839870c5c68b5909bff510&type=album'
    await message.answer(
        'COPYWRITING\nWe have been working in the field of copywriting since 2020 and already have a lot of experience in this topic.\n\nOrder - Contact our administrator (Telegram - @n1kkostyle)')
    await bot.send_photo(chat_id, photo=photo_url)

@dp.message(Text(text='Telegram bots'))
async def show_copywriting(message: Message):
    chat_id = message.from_user.id
    photo_url = 'https://sun9-59.userapi.com/impg/9WGAfmYhHI8wKaR4MQeP3BJZgCfp1LB6MdZajA/WfiA1blCdTQ.jpg?size=1024x1024&quality=95&sign=398d8fa008b949d002c676576b28fe44&c_uniq_tag=oaWGtlLmwlQhyrXpEkPEksaFk7OPSetgzp2qSwUR5yc&type=album'
    await message.answer(
        'Telegram bots\nWe have created many telegram bots and received a lot of positive feedback.\nWe write bots in the Python programming language and use the aiogram library.\n\nOrder - Contact our administrator (Telegram - @n1kkostyle)')
    await bot.send_photo(chat_id, photo=photo_url)


if __name__ == '__main__':
    dp.run_polling(bot)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
