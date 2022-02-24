from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.ichimlik import ichmlik
from states.kofee import Kofee

@dp.message_handler(text='ichimlik', state=Kofee.category)
async def get_men(message: types.Message, state: FSMContext):
    cat = message.text
    await state.update_data(
        {'cat': cat}
    )
    await message.answer("batafsil malumot uchun ichimlikni tanlang", reply_markup=ichmlik)
    await Kofee.next()