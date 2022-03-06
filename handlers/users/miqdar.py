from aiogram import types
from keyboards.default.baliq import balq
from keyboards.default.ichimlik import ichmlik
from keyboards.default.ovqat2 import ovqat
from loader import dp, db
from aiogram.dispatcher import FSMContext
from states.kofee import Kofee
from handlers.users.narxi import price


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@dp.message_handler(state=Kofee.amaunt)
async def orqa1(message: types.Message, state: FSMContext):
    n = message.text
    if is_number(n) == True:
        data = await state.get_data()
        od = data.get('odi')
        cat = data.get('cat')
        # nn = price[od]* int(n)
        if cat == 'Baliq':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=balq)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kofee.amaunt.set()
        elif cat == 'ichimlik':
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=ichmlik)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kofee.product.set()
        elif cat == "Ikkinchi ovqatlar":
            await message.answer(f"{od} <i>dan {n} ta, savatchaga🛒 qo'shildi</i>", parse_mode='html')
            await message.answer("Xo'sh <i>davom etamizmi 😍?</i>",'html', reply_markup=ovqat)
            product = db.check_product(tg_id=message.from_user.id, Product=od)
            if product:
                db.update_product(tg_id=message.from_user.id, Product=od, quantity=int(product[2]) + int(n))
            else:
                db.add_product(tg_id=message.from_user.id, Product=od, quantity=n)
            await Kofee.product.set()
      
    else:
        await message.answer("Faqat son kiriting!")
        await Kofee.amaunt.set()