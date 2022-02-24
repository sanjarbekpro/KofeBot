from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cats = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Baliq'), KeyboardButton(text='ichimlik')],
        [KeyboardButton(text='Ikkinchi ovqatlar'), KeyboardButton(text='Orqaga')]
    ],
    resize_keyboard=True
)