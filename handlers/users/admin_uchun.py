from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu_uchun import menu_buttons, tasdiqlash_buttons
from loader import dp, bot
from states.holatlar import Forma

# Echo bot
@dp.message_handler(text="Adminga murojat")
async def bot_echo(message: types.Message):
    await message.answer(text= "Ismni kiriting")
    await Forma.ism_qabul_qilish.set()

@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message , state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text= "Familyani kiriting")
    await Forma.fam_qabul_qilish.set()

@dp.message_handler(state=Forma.fam_qabul_qilish)
async def bot_echo(message: types.Message , state:FSMContext):
    famliya = message.text
    await state.update_data({'fam':famliya})
    await message.answer(text= "Yoshni kiriting")
    await Forma.yosh_qabul_qilish.set()

@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message , state:FSMContext):
    age = message.text
    await state.update_data({'yoshi':age})
    await message.answer(text= "Murojatni kiriting")
    await Forma.tg_akkaunt.set()

@dp.message_handler(state=Forma.tg_akkaunt)
async def bot_echo(message: types.Message , state:FSMContext):
    tg = message.text
    await state.update_data({'tg':tg})
    await message.answer(text= "Telegarm akauntni kiriting")
    await Forma.matn_qabul_qilish.set()


@dp.message_handler(state=Forma.matn_qabul_qilish)
async def bot_echo(message: types.Message , state:FSMContext):
    text = message.text
    await state.update_data({'matn':text})
    malumot = await state.get_data()
    ism = malumot.get("name")
    fami = malumot.get("fam")
    yosh = malumot.get("yoshi")
    telegram = malumot.get("tg")
    matn = malumot.get("matn")
    s = f"Ism : {ism} \n" \
        f"Familyasi : {fami} \n" \
        f"Yoshi : {yosh} \n" \
        f"Telegram akauntiz: {matn} \n" \
        f"Murojatni : {telegram} \n"
    await bot.send_message(chat_id=message.from_user.id,text=s , reply_markup=tasdiqlash_buttons)

    await Forma.tasdiqlash.set()

@dp.message_handler(state=Forma.tasdiqlash, text="Tasdiqlash")
async def bot_echo(message: types.Message, state: FSMContext):
    malumot = await state.get_data()
    ism = malumot.get("name")
    fami = malumot.get("fam")
    yosh = malumot.get("yoshi")
    telegram = malumot.get("tg")
    matn = malumot.get("matn")
    s = f"Ism : {ism} \n" \
        f"Familyasi : {fami} \n" \
        f"Yoshi : {yosh} \n" \
        f"Telegram akauntiz: {matn} \n" \
        f"Murojatni : {telegram} \n"
    await bot.send_message(chat_id=1120480340, text=s)
    await bot.send_message(chat_id=message.from_user.id,text="Adminga yuborildi")
    await state.finish()

@dp.message_handler(state=Forma.tasdiqlash, text="Bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="Bekor qilindi" , reply_markup=menu_buttons)
    await state.finish()


@dp.message_handler(text='orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Orqaga qaytingiz, {message.from_user.full_name}!",reply_markup=menu_buttons )