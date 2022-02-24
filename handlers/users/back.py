from loader import dp
from aiogram import types
from states.kofee import Kofee
from keyboards.default.asosiy import menu
from keyboards.default.catigory import cats
from keyboards.default.baliq import balq
from aiogram.dispatcher import FSMContext
from keyboards.default.ichimlik import ichmlik


@dp.message_handler(text="Orqaga", state=Kofee.category)
async def back_cat(message: types.Message, state: FSMContext):
	await message.answer("Sahifani tanlang 😊", reply_markup=menu)
	await state.finish()


@dp.message_handler(text="Orqaga", state=Kofee.product)
async def back_prod(message: types.Message):
	await message.answer("Taomlarga o'tish uchun sahifani tanlang...", reply_markup=cats)
	await Kofee.category.set()


@dp.message_handler(text="Orqaga", state=Kofee.amaunt)
async def back_amount(message: types.Message, state: FSMContext):
	data = await state.get_data()
	cat = data.get('cat')
	if cat == "Baliq":
		await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=balq)
	elif cat == "ichimlik":
		await message.answer("Batafsil ma'lumot uchun taomni tanlang", reply_markup=ichmlik)
	await Kofee.product.set()


# @dp.message_handler(text="Bosh Sahifa 🏠", state=Kofee.amaunt)
# async def back_amount(message: types.Message, state: FSMContext):
# 	await message.answer("Buyurtma berishni boshlaymizmi?", reply_markup=menu)
# 	await state.finish()