from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Biz haqimizda'),
            KeyboardButton(text='Darslar haqida')
        ],
        [
            KeyboardButton(text='PDP Univerite ga kirish uchun'),
            KeyboardButton(text="Zakovat o'yinlari")
        ],
        [
            KeyboardButton(text='Adminga murojat'),

        ]
    ],
    resize_keyboard=True
)

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tasdiqlash'),
            KeyboardButton(text='Bekor qilish')
        ],
        [
            KeyboardButton(text='orqaga'),
        ],

    ],
    resize_keyboard=True
)