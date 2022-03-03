# from loader import dp
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from keyboards.default.baliq import balq
# from states.kofee import Kofee

# @dp.message_handler(text='Baliq', state=Kofee.category)
# async def get_men(message: types.Message, state: FSMContext):

#     boliq = message.text
#     data = await state.get_data()
    
#     if 'cart' in data.keys():
#         cart = data.get('cart')
#         await state.update_data(
#             {
#                 'cart': cart
#             }
#         )
#     else:
#         await state.update_data(
#             {'cat':boliq, 'cart': []},
#         )
#     # cat = message.text
#     # await state.update_data(
#     #     {'cat': cat}
#     # )
#     await message.answer("batafsil malumot uchun taomni tanlang", reply_markup=balq)
#     await Kofee.next()

