from aiogram import types

from loader import dp, bot


# Echo bot
@dp.message_handler(text="PDP Univerite ga kirish uchun")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/384'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
    ⏳ OYMA-OY KAMAYIB BORUVCHI IMTIYOZNI QO'LDAN BOY BERMANG!

🏛 PDP University Kirish imtihonlaridan o'tib, talabalikka tavsiya etilsangiz:

✅ To'lov shartnomasini 100% to'lamoqchi bo'lganlarga katta chegirmalar taqdim etamiz. Ushbu imkoniyatdan mart oyida unumli foydalanganlar yillik 36 mln so'm emas, 26 mln so'm kontrakt to'lashdi.

📌 Aprel oyida 100% to'lamoqchi bo'lganlar uchun ushbu miqdor — 27 mln so'm etib belgilandi.

‼️ Oyma-oy ushbu imtiyoz miqdori kamayib, kontrakt summasi asl narxiga yaqinlashib boraveradi.

🤾🏻‍♂️ SHOSHILING!

⚡️ USHBU IMKONIYATDAN UNUMLI FOYDALANIB QOLING!

👇 KIRISH IMTIHONLARIGA RO'YXATDAN O'TISH:

➡️ Viloyatlar va Qoraqalpog‘istonda
 (https://forms.amocrm.ru/rrrdrrd)‼️ 23 aprel // 9:00 

➡️ Toshkent shahrida (https://forms.amocrm.ru/rlmdwrd) 
‼️ 15 aprel // 10:00


📞 78-777-77-47

Telegram (https://t.me/pdpuniversity) | Instagram (https://www.instagram.com/pdp.university/) | YouTube (https://www.youtube.com/channel/UCjpbksOprX8kSciHQY6yupw/)
    """)


@dp.message_handler(text="Darslar haqida")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/4'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
    🎯 PDP University Mission

🚀 Har bir oliy ta'lim muassasasi o'z oldiga ma'lum bir sohada yetuk kadrlarni tayyorlashni maqsad qilib olganidek, PDP University ham katta rejalar bilan o'z faoliyatini boshlamoqda.

🟢// PDP University — to'laqonli IT sohasiga ixtisoslashgan universitet bo'lib, o'z oldiga raqamli texnologiyalar yordamida dunyoni yaxshi tarafga o’zgartira oladigan mutaxassislarni tayyorlash, shu sohada sifatli mahsulot va xizmatlarni ishlab chiqarishni maqsad qilib qo'ygan.

🧗🏻 Albatta ko'zlangan natijaga erishish uchun jamoamizda ko'plab professionallar mehnat qilishmoqda va tez kunda talabalarni qabul qilishni boshlaymiz.

☎️ 78-777-47-47

Telegram (https://t.me/pdpuniversity) | Instagram (https://www.instagram.com/pdp.university/) | Web-site (https://university.pdp.uz/)
    """)


@dp.message_handler(text="Biz haqimizda")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/5'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
⏳ PDP Ecosystem tarixi

🟢// PDP Academy'ga 2017-yilda Odilbek Mirzayev tomonidan asos solingan.

🏢 Akademiya dastlabki faoliyatini 240 talabaga mo'ljallangan, 180 kv/m binoda boshlagan va 2019-yilga kelib 600 kv/m maydonga ega binoga ko'chirilgan. 

🚀 2021-yilga kelib talabalar soni oshishi — yangi, kattaroq o'quv binosiga ko'chishga sabab bo'ldi va PDP Academy o'z faoliyatini 3000 kv/m maydonli, 3000 talabaga mo'ljallangan binoda davom ettirib kelmoqda.

☎️ 78-777-47-47

Telegram (https://t.me/pdpuniversity) | Instagram (https://www.instagram.com/pdp.university/) | Web-site (https://university.pdp.uz/)
    """)


@dp.message_handler(text="Zakovat o'yinlari")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/388'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
[ Album ]
🏛 PDP University: "Students' Union" Prezidentini saylashda ishtirok eting!
📃 Nomzodlar bilan tanishing:
☑️ Temirov Bekzodbek

Tug'ilgan vaqti va joyi: 12.03.2005 
Saylovoldi dasturi: Talabalar va universitetlar o'rtasida Hakatonlar, Zakovat o'yinlari va Kibersport bo'yicha musobaqalar tashkil etish, ijtimoiy tarmoqlar orqali universitet talabalarining hayotini faol aks ettirish uchun Media bo'limi bilan hamkorlikda sifatli kontentlar yaratish.
☑️ Turdiyev Abdurahmon

Tug'ilgan vaqti va joyi: 17.10.2004 
Saylovoldi dasturi: Talabalar o'rtasida jamoaviy ishlash ko'nikmalarini shakllantirish, turli yo'nalishlarda  o'zaro munosabat qurishda ko'maklashish, chet tillarini ommalashtirish, mahalliy va xalqaro universitetlar bilan aloqalar o'rnatish.
☑️ Umurzoqov Abdulaziz

Tug'ilgan vaqti va joyi: 23.10.2002 
🌐 PDP University — raqamli taʼlim, raqamli kelajak yaratish uchun! """)


    #english tili



@dp.message_handler(text="About us")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/5'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
⏳ History of PDP Ecosystem

🟢// PDP Academy was founded in 2017 by Odilbek Mirzayev.

🏢 The academy started its initial activity in a building of 180 sq/m for 240 students and by 2019 it was moved to a building with an area of 600 sq/m.

🚀 By 2021, the increase in the number of students led to the move to a new, larger educational building, and PDP Academy continues to operate in a 3,000-square-meter building with a capacity of 3,000 students.

☎️ 78-777-47-47

Telegram (https://t.me/pdpuniversity) | Instagram (https://www.instagram.com/pdp.university/) | Website (https://university.pdp.uz/)
""")


@dp.message_handler(text="Intelligence games")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/388'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
[ Album ]
🏛 PDP University: Participate in the election of the President of the "Students' Union"!
📃 Meet the candidates:
☑️ Temirov Bekzodbek

Time and place of birth: 12.03.2005
Electoral program: Organization of Hackathons, Zakovat games and Cybersport competitions between students and universities, creation of quality content in cooperation with the Media department to actively reflect the life of university students through social networks.
☑️ Turdiyev Abdurakhman

Time and place of birth: 17.10.2004
Electoral program: formation of teamwork skills among students, assistance in building mutual relations in various directions, popularization of foreign languages, establishment of relations with local and international universities.
☑️ Umurzokov Abdulaziz

Time and place of birth: 23.10.2002
🌐 PDP University — digital education, to create a digital future! """)


@dp.message_handler(text="About lessons")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/4'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
  🎯 PDP University Mission

🚀 As every higher education institution aims to train skilled personnel in a certain field, PDP University is starting its activities with big plans.

🟢// PDP University is a full-fledged university specializing in the field of IT, which aims to train specialists who can change the world for the better with the help of digital technologies, and to produce quality products and services in this field.

🧗🏻 Of course, many professionals are working in our team to achieve the desired result, and we will soon start accepting students.

☎️ 78-777-47-47

Telegram (https://t.me/pdpuniversity) | Instagram (https://www.instagram.com/pdp.university/) | Website (https://university.pdp.uz/)  """)


@dp.message_handler(text="To enter PDP University")
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/pdpuniversity/384'
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili, caption="""
    ⏳ DON'T MISS THE PRIVILEGE THAT DECREASES MONTHLY!

🏛 If you pass the PDP University entrance exams and are recommended for studentship:

✅ We offer big discounts to those who want to pay 100% of the payment contract. Those who took advantage of this opportunity in March paid a contract of 26 million soums instead of 36 million soums per year.

📌 For those who want to pay 100% in April, this amount is set at 27 million soums.

‼️ Month by month, the amount of this benefit decreases, and the contract amount gets closer to the original price.

🤾🏻‍♂️ HURRY UP!

⚡️ TAKE ADVANTAGE OF THIS OPPORTUNITY!

👇 REGISTRATION FOR ENTRANCE EXAMS:

➡️ Regions and Karakalpakstan
  (https://forms.amocrm.ru/rrrdrrd)‼️ April 23 // 9:00

➡️ in Tashkent (https://forms.amocrm.ru/rlmdwrd)
‼️ April 15 // 10:00


📞 78-777-77-47

Telegram (https://t.me/pdpuniversity) | Instagram (https://www.instagram.com/pdp.university/) | YouTube (https://www.youtube.com/channel/UCjpbksOprX8kSciHQY6yupw/)""")
