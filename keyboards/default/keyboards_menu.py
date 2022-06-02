from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
        ],
        [
            KeyboardButton(text='77'),
        ],
        [
            KeyboardButton(text='777'),
        ]
    ],
    resize_keyboard=True
)