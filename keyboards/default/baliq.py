from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balq = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Sazan(300g)'), KeyboardButton(text='Sudak(300g)')],
        [KeyboardButton(text='Sous(300ml)'), KeyboardButton(text='Savatcha')],
        [KeyboardButton(text='Orqaga')]
    ],
    resize_keyboard=True
)