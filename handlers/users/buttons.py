from aiogram import types
from loader import dp

@dp.message_handler(text='7')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'ты выбрал {message.text}')

@dp.message_handler(text='8')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'ты выбрал {message.text}')

@dp.message_handler(text='77')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'ты выбрал {message.text}')

@dp.message_handler(text='777')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'ты выбрал {message.text}')