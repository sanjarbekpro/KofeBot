from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Menu'), KeyboardButton(text='Savatcha')]
    ],
    resize_keyboard=True
)