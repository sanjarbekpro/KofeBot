from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.miqdor import miqdorlar
from states import kofee
from states.kofee import Kofee

@dp.message_handler(text='Coca-cola(0,5 l)', state=Kofee.product)
async def get_cola(message: types.Message):
    await message.answer("Coca-cola(0,5l-6000 so'm)")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Fanta(0,5 l)', state=Kofee.product)
async def get_fanta(message: types.Message):
    await message.answer("Fanta(0,5l-6000 so'm)")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Coca-cola(1,5 l)', state=Kofee.product)
async def get_col(message: types.Message):
    await message.answer_photo(photo="https://ibb.co/zsT5SnF", caption="Coca-cola(1 l-12000 so'm)")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Fanta(1,5 l)', state=Kofee.product)
async def get_fan(message: types.Message):
    await message.answer("Fanta(1 l-12000 so'm)")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()