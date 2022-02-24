from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ovqat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Мишель'), KeyboardButton(text='Мясо по-французски')],
        [KeyboardButton(text='Fri 🍟'), KeyboardButton(text='Orqaga')]
    ],
    resize_keyboard=True
)