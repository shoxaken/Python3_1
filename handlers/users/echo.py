from aiogram import types

from loader import dp
from filters import Shaxsiy


# Echo bot
@dp.message_handler(Shaxsiy() , state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
