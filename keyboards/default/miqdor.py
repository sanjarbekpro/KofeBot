from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

miqdorlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='1'), KeyboardButton(text='2')],
        [KeyboardButton(text='3'), KeyboardButton(text='4')],
        [KeyboardButton(text='Orqaga')]
    ],
    resize_keyboard=True
)