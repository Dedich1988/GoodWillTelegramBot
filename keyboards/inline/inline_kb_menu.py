from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_widh=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='🔗 Реферальная ссылка', callback_data='🔗 Реферальная ссылка'),
                                        InlineKeyboardButton(text='Ссылка', url='https://github.com/Dedich1988'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='alert', callback_data='alert')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Заменить кнопки меню', callback_data='кнопки2')
                                    ]
                                ])
