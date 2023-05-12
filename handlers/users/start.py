from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.for_menu import menu_button
from keyboards.inline.tillar_uchun import tillar_buttons
from middlewares.majburi_azolik import Asosiy_checking
from filters import Shaxsiy
from loader import dp

@dp.message_handler(Shaxsiy(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)

@dp.callback_query_handler(text="til1")
async def bot_start(xabarlar: CallbackQuery):
    await xabarlar.message.answer(f"menu tanlang, ", reply_markup=menu_buttons)

@dp.callback_query_handler( text="til2")
async def bot_start(xabarlar: CallbackQuery):
    await xabarlar.message.answer(f"menu choose, ", reply_markup=menu_button)



@dp.callback_query_handler(text="www")
async def bot_start(xabarlar: CallbackQuery):
    await xabarlar.message.answer(f"menu tanlang, ", reply_markup=menu_buttons)

@dp.message_handler(Shaxsiy(), text='orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Orqaga qaytingiz, {message.from_user.full_name}!",reply_markup=menu_buttons )

@dp.message_handler(Shaxsiy(), text='back')
async def bot_start(message: types.Message):
    await message.answer(f"go back, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(Shaxsiy(), commands="boshlash")
async def bot_start(message: types.Message):
    await message.answer(f"Salom,botga hush kelibsi!")
