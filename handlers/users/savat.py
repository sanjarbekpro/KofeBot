from loader import dp, db
from aiogram import types
from states.kofee import Kofee
from handlers.users.narxi import get_price
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(text='Savatcha')
async def korzina(message: types.Message):
    try:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Buyurtma berish 🚚")
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Sizning buyurtmalaringiz\n\n"
        for product in products:
            markup.add(f"❌ {product[1]} ❌")
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} so'm\n"

        msg += f"\nUmumiy narx: {total} so'm"
        markup.row("Orqaga", "Bo'shatish 🗑")
        await message.answer(msg, reply_markup=markup)
    except:
        await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")

@dp.message_handler(text='Savatcha', state=Kofee.category)
async def korzina(message: types.Message):
    try:
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Sizning buyurtmalaringiz\n\n"
        for product in products:
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} so'm\n"

        msg += f"\nUmumiy narx: {total} so'm"
        await message.answer(msg)
    except:
        await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")

# @dp.message_handler(text='Savatcha 🛒', state=anketa.category)
# async def korzina(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     try:
#         msg = "Sizning buyutmalaringiz\n"
#         total = 0
#         if 'cart' in data.keys():
#             cart = data['cart']
#             for c in cart:
#                 narx = get_price(c['name'], c['amount'])
#                 msg += f"{c['name']} x {c['amount']} = {narx} so'm\n"
#                 total += narx
#         msg += f"\nUmumiy narx: {total} so'm"
#         await message.answer(msg)
#     except:
#         await message.answer("Savatchangiz bo'sh biror nima buyurtirmaysizmi?")




@dp.message_handler(text='Savatcha', state=Kofee.product)
async def korzina(message: types.Message):
    try:
        products = db.get_products(tg_id=message.from_user.id)
        total = 0
        msg = "Sizning buyurtmalaringiz\n\n"
        for product in products:
            price = get_price(product[1], product[2])
            total += price
            msg += f"{product[1]} x {product[2]} = {price} so'm\n"

        msg += f"\nUmumiy narx: {total} so'm"
        await message.answer(msg)
    except:
        await message.answer("Savatchangiz bo'sh iltimos biror nima buyurtring!")
    