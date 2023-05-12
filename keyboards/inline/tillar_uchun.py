from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili" , callback_data="til1"),
            InlineKeyboardButton(text="ingiliz tili" , callback_data="til2")
        ],
        [
            InlineKeyboardButton(text="Admin bilan bog'lanish" , url="https://t.me/SHOX_AKEN_SHOX"),
        ]
    ]
)