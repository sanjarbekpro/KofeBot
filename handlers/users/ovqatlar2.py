from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.miqdor import miqdorlar
from states.kofee import Kofee


@dp.message_handler(text='Мишель', state=Kofee.product)
async def get_men(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo(photo="https://ibb.co/LZSJWn2",caption="Мишель\n\nNarxi: 30000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Мясо по-французски', state=Kofee.product)
async def get_men(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo(photo="https://ibb.co/Sf4gWVf",caption="Мясо по-французски\n\nNarxi: 28000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Fri 🍟', state=Kofee.product)
async def get_men(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo(photo="https://ibb.co/GFJWh4L",caption="Fri 🍟\n\nNarxi: 10000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()