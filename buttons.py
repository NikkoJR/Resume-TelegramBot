from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo


insta = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Our instagram',
            url='https://www.instagram.com/ldln.official/'
        )
    ]
])

portfolio = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Our portfolio',
            url='https://docs.google.com/presentation/d/16GXJO_vV7cloy6cvbJYI4Ev7TsCBCDc5T833A29ug38/edit?usp=sharing'
        )
    ]
])

responsibilities = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Our responsibilities',
            url='https://docs.google.com/presentation/d/16GXJO_vV7cloy6cvbJYI4Ev7TsCBCDc5T833A29ug38/edit?usp=sharing'
        )
    ]
])

adm_profile = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Admin pofile',
            url='https://t.me/n1kkostyle'
        )
    ]
])