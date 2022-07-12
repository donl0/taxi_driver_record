import types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


keyboard_back = ReplyKeyboardMarkup(row_width=1)
back_button = KeyboardButton(text='Назад')
keyboard_back.add(back_button)


