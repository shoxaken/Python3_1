from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='About us'),
            KeyboardButton(text='About lessons')
        ],
        [
            KeyboardButton(text='To enter PDP University'),
            KeyboardButton(text='Intelligence games')
        ]
    ],
    resize_keyboard=True
)