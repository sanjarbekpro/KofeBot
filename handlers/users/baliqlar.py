from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.miqdor import miqdorlar
from keyboards.default.baliq import balq
from states.kofee import Kofee

@dp.message_handler(text='Baliq', state=Kofee.category)
async def get_men(message: types.Message, state: FSMContext):
    cat = message.text
    data = await state.get_data()
    
    if 'cart' in data.keys():
        cart = data.get('cart')
        await state.update_data(
            {
                'cart': cart
            }
        )
    else:
        await state.update_data(
            {'cat':cat, 'cart': []},
        )
    await message.answer("batafsil malumot uchun taomni tanlang", reply_markup=balq)
    await Kofee.next()





@dp.message_handler(text='Sazan(300g)', state=Kofee.product)
async def fish(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo(photo="https://ibb.co/BcWY7Fd",caption="Sazan (300g)\n\nNarxi: 45000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Sudak(300g)', state=Kofee.product)
async def get_menu(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo(photo="https://ibb.co/4dM4P19",caption="Sudak (300g)\n\nNarxi: 48000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()

@dp.message_handler(text='Sous(300ml)', state=Kofee.product)
async def get_menu(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'odi':cat}
    )
    await message.answer_photo(photo="https://ibb.co/gttkrKt",caption="Sous 300ml\n\nNarxi: 7000 so'm")
    await message.answer("Maxsulotni Savatga🛒 qo'shish uchun, sonini kiriting 👇🏼", reply_markup=miqdorlar)
    await Kofee.next()