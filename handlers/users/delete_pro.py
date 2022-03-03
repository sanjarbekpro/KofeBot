from aiogram.types import ReplyKeyboardRemove
from loader import dp, db
from aiogram import types



@dp.message_handler(text_contains="❌")
async def delete_product(message: types.Message):
    product = message.text
    product = product.replace("❌", "")
    db.delete_product(tg_id=message.from_user.id, Product=product.strip())
    await message.answer(f"{product.strip()} savatingiz o'chirildi!", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Bo'shatish 🗑")
async def clearcart(message: types.Message):
    id = message.from_user.id
    db.clear_cart(tg_id=id)
    await message.answer("Savatchnagiz tozalandi!", reply_markup=ReplyKeyboardRemove())