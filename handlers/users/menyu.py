from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.catigory import cats
from states.kofee import Kofee

@dp.message_handler(text='Menu')
async def get_menu(message: types.Message):
    await message.answer("Xo'sh buyurmaga o'tamizmi", reply_markup=cats)
    await Kofee.category.set()