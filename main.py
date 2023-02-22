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
import sqlite3


# Connect to bot in TG
bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


# Create buttons
button_to_show_copywriting: KeyboardButton = KeyboardButton(text='Copywriting')
button_to_show_Tbots: KeyboardButton = KeyboardButton(text='Telegram bots')

button_to_log_in: KeyboardButton = KeyboardButton(text='Log in')
button_to_sing_up: KeyboardButton = KeyboardButton(text='Sing up')
button_to_continue: KeyboardButton = KeyboardButton(text='Continue as a guest')

# Create keyboards
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_to_show_copywriting], [button_to_show_Tbots]],
                                    resize_keyboard=True,
                                    one_time_keyboard=True)

keyboard_in: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_to_log_in], [button_to_sing_up], [button_to_continue]],
                                    resize_keyboard=True,
                                    one_time_keyboard=True)


#lists of user and his id to sing up / log in process

user: dict = {'login': '',
              'password': '',
              'id': False}

user_choices_in_login: dict = {'login': '',
                                'password': ''}

authorization_logs: dict = {'id_log': False,
                          'id_log_sing_up': False,
                          'id_sing_up_log': False,
                          'id_sing_up_sing_up': False,
                          'authorization_id': False,
                          'guest_log': False}


#Base of date

bd = sqlite3.connect('LDLN.bd')
cur = bd.cursor()

bd.execute('CREATE TABLE IF NOT EXISTS {}(login TEXT, password TEXT)'.format('users'))
bd.commit()


print('Bot is ON')



#hendlers to commands

@dp.message(CommandStart())
async def start_process(message: Message):
    await message.answer("Hi! It's LDLN bot. \nYou can push on menu button to see commands. \nTo get more info - /help\n Do you have an account? If not, you can register", reply_markup=keyboard_in)

@dp.message(Text(text='/log'))
async def log_process(message: Message):
    await message.answer('Would you like to log in or you have an account?', reply_markup=keyboard_in)


@dp.message(Text(text='/help'))
async def help_process(message: Message):
    await message.answer(
'This bot was created by the LDLN team. \nWith it, you will be able to use our resources without any difficulty. \n\nIn addition, you can contact our administrator who will help you.\n\nIn the menu tab you can find shortcut commands\nAll commands available for use:\n/help\n/start\n/info\n/insta\n/portfolio\n/responsibilities\n/adm_profile\n/login (Only for admins team)\n/products\n/log - to log in or sing up')

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

@dp.message(Text(text='Continue as a guest'))
async def continue_as_a_guest(message: Message):
    await message.answer('System message: You are logged in as a guest')
    authorization_logs['guest_log'] = True





#Hendlers to log in and sing up


#process starting after command "sing up"
@dp.message(Text(text='Sing up'))
async def sing_up(message: Message):
    authorization_logs['id_sing_up_log'] = True
    await message.answer('Create new login and password')
    await message.answer('System message: Write your new login')

@dp.message(lambda x: x.text and authorization_logs['id_sing_up_log'] == True)
async def process_sing_up_login(message: Message):
    login = message.text
    check_logs = cur.execute('SELECT password FROM users WHERE login == ?', (login,)).fetchone()

    if check_logs != None:
        await message.answer('System message: This login is already took')
        await message.answer('Please try again.')

        authorization_logs['id_sing_up_log'] = False


    elif check_logs == None:
        authorization_logs['id_sing_up_sing_up'] = True
        await message.answer('System message: Write your new password')
        user['login'] = login
        authorization_logs['id_sing_up_log'] = False


@dp.message(lambda x: x.text and authorization_logs['id_sing_up_sing_up'] == True)
async def process_sing_up_password(message: Message):
    login = user['login']
    password = message.text
    user['password'] = password
    print(f'User singed up, his login - {login}, his password - {password}')
    user['id'] = True
    cur.execute('INSERT INTO users (login, password) VALUES (?, ?)', (login, password))
    bd.commit()

    print('Данные были добавлены в таблицу')
    await message.answer('You have successfully created accout')
    authorization_logs['id_sing_up_sing_up'] = False



#process starting after command "log in"
@dp.message(Text(text='Log in'))
async def login_in(message: Message):
    authorization_logs['id_log'] = True
    await message.answer('System message: Write your login')



@dp.message(lambda x: x.text and authorization_logs['id_log'] == True)
async def process_login(message: Message):
    user['login'] = message.text
    login = message.text
    password = cur.execute('SELECT password FROM users WHERE login == ?', (login,)).fetchone()

    if password != None:

        password = str(password)
        for i in password:
            if i == '(' or i == ')' or i == ',' or i == "'":
                password = password.replace(i, '')

        user['password'] = password

        await message.answer(f'Hello {login}.')
        await message.answer('Write your password')

        authorization_logs['id_log'] = False
        authorization_logs['id_log_sing_up'] = True

    elif password == None:
        await message.answer('System message: Your login is not found!')
        authorization_logs['id_log'] = False


@dp.message(lambda x: x.text and authorization_logs['id_log_sing_up'] == True)
async def process_login(message: Message):
    password = message.text
    if password == user['password']:
        print(f'User logs in, his login and password - ', user['login'], user['password'])
        await message.answer('System message: You have successfully login in your account')
        authorization_logs['id_log_sing_up'] = False
        authorization_logs['authorization_id'] = True


    elif password != user['password']:
        print('User ', user['login'], 'did not connect to his account')
        await message.answer('Password is incorrent. Try again!')
        authorization_logs['id_log_sing_up'] = False



#message to unknown commands or messages
@dp.message(lambda x: x.text)
async def process_login(message: Message):
    await message.answer("I can't perform functions I'm not designed for!")


if __name__ == '__main__':
    dp.run_polling(bot)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

