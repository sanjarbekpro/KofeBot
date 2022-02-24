from keyboards.default.baliq import balq
from keyboards.default.ichimlik import ichmlik
from keyboards.default.ovqat2 import ovqat
from loader import dp
from aiogram import types
from states.kofee import Kofee
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=Kofee.amaunt)
async def order(message: types.Message, state: FSMContext):
	amaunt = message.text
	await state.update_data({
		'amaunt': amaunt
	})
	data = await state.get_data()
	cat = data.get('cat')
	if cat == "Baliq":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=balq)
	elif cat == "ichimlik":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=ichmlik)
	elif cat == "Ikkinchi ovqatlar":
		await message.answer("Savatchaga🛒 qo'shildi")
		await message.answer("Xo'sh davom etamizmi 😍?", reply_markup=ovqat)
	await Kofee.product.set()