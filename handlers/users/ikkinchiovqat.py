from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.ovqat2 import ovqat
from states.kofee import Kofee

@dp.message_handler(text='Ikkinchi ovqatlar', state=Kofee.category)
async def get_men(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("batafsil malumot uchun ichimlikni tanlang", reply_markup=ovqat)
    await Kofee.next()