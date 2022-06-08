from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.default import kb_test
from keyboards.inline import ikb_menu, ikb_menu2
from loader import dp


@dp.message_handler(text='Inline Keyboards')
async def show_inline_menu(message: types.Message):
    await message.answer('Инлайн кнопки ниже', reply_markup=ikb_menu)

@dp.callback_query_handler(text='кнопки2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)

@dp.callback_query_handler(text='alert')
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки заменены', show_alert=True)

@dp.callback_query_handler(text='кнопки1')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu)