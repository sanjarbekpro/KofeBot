from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ichmlik = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Coca-cola(0,5 l)'), KeyboardButton(text='Fanta(0,5 l)')],
        [KeyboardButton(text='Coca-cola(1,5 l)'), KeyboardButton(text='Fanta(1,5 l)')],
        [KeyboardButton(text='Orqaga')]
    ],
    resize_keyboard=True
)