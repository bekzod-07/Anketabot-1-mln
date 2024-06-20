from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime

from keyboards.default.Menu import bosh_menu
from keyboards.default.chek import check_rus
from keyboards.default.hammasi import hammasi_rus
from keyboards.default.ishorin import ishorin_rus
from keyboards.default.jins import jins_rus
from keyboards.default.komppp import komp_rus
from keyboards.default.mal import mall_rus
from keyboards.default.mayka import mayka_rus
from keyboards.default.talim_shakli import talim_shakli_rus
from keyboards.default.tuman import tum_rus
from keyboards.default.viloyat import vil_rus
from keyboards.default.yoq import yoq_rus
from keyboards.default.ish import ish_rus
from loader import dp, bot
from states.rus_state import rus_state


from aiogram.dispatcher.filters import Text

valid_viloyatlar = ["Бухарская область"]
valid_tumanlar = ["Шафирканский район", "Ромитанский район"]

@dp.message_handler(Text(equals="Отменить 🚫"), state='*')
async def cancel_action(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Выберите нужное меню", reply_markup=bosh_menu)

@dp.message_handler(text="🇷🇺 Русский язык 🇷🇺", state=None)
async def enter_test(message: types.Message):
    await message.answer("Введите ваше полное имя\n\nФИО (Гафуров Лочинбек Фахриддин угли) в формате: 📋", reply_markup=hammasi_rus)
    await rus_state.fio.set()

@dp.message_handler(state=rus_state.fio)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"ФИО": fullname})
    await message.answer("📅 Дата рождения :\n\nДД.ММ.ГГГГ (15.10.2007) в формате:", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.date)
async def answer_date(message: types.Message, state: FSMContext):
    date_str = message.text
    try:
        date = datetime.strptime(date_str, "%d.%m.%Y")

        if date.year > 2024:
            await message.answer("Год вашего рождения не может быть позже 2024.", reply_markup=hammasi_rus)
        else:
            await state.update_data({"Дата": date_str})
            await message.answer("Выберите область", reply_markup=vil_rus)
            await rus_state.next()
    except ValueError:
        await message.answer("Пожалуйста, введите дату рождения в правильном формате (ДД.ММ.ГГГГ).", reply_markup=hammasi_rus)


@dp.message_handler(state=rus_state.viloyat)
async def answer_viloyat(message: types.Message, state: FSMContext):
    viloyat = message.text
    if viloyat in valid_viloyatlar:
        await state.update_data({"Область": viloyat})
        await message.answer("Выберите район", reply_markup=tum_rus)
        await rus_state.next()
    else:
        await message.answer("Пожалуйста, выберите область из предложенных вариантов.", reply_markup=vil_rus)

@dp.message_handler(state=rus_state.tuman)
async def answer_tuman(message: types.Message, state: FSMContext):
    tuman = message.text
    if tuman in valid_tumanlar:
        await state.update_data({"Район": tuman})
        await message.answer("Введите вашу профессию", reply_markup=hammasi_rus)
        await rus_state.next()
    else:
        await message.answer("Пожалуйста, выберите район из предложенных вариантов.")

@dp.message_handler(state=rus_state.kasbi)
async def answer_kasb(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data({"Профессия": kasb})
    await message.answer("Выберите ваш пол", reply_markup=jins_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.jinsi)
async def answer_jins(message: types.Message, state: FSMContext):
    jins = message.text
    if jins in ["Мужской", "Женский"]:
        await state.update_data({"Пол": jins})
        await message.answer("Какая у вас специализация?", reply_markup=hammasi_rus)
        await rus_state.next()
    else:
        await message.answer("Пожалуйста, выберите пол из предложенных вариантов.", reply_markup=jins_rus)


@dp.message_handler(state=rus_state.mutaxasislik)
async def answer_mutaxasislik(message: types.Message, state: FSMContext):
    mutaxasisligi = message.text
    await state.update_data({"Специализация": mutaxasisligi})
    await message.answer("На какой должности вы хотите работать?", reply_markup=ish_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.ishlash_lavozimi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    lavozim = message.text
    await state.update_data({"Должность": lavozim})
    await message.answer("Сколько лет у вас опыта работы?", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.ish_tajriba)
async def answer_tajriba(message: types.Message, state: FSMContext):
    tajriba = message.text
    if tajriba.isdigit():
        await state.update_data({"Опыт": tajriba})
        await message.answer("Введите ваш номер телефона", reply_markup=hammasi_rus)
        await rus_state.next()
    else:
        await message.answer("Пожалуйста, введите только цифры.", reply_markup=hammasi_rus)

@dp.message_handler(state=rus_state.tele_raqam)
async def answer_raqam(message: types.Message, state: FSMContext):
    raqam = message.text
    if raqam.startswith("+998") and len(raqam) == 13 and raqam[1:].isdigit():
        await state.update_data({"Номер телефона": raqam})
        await message.answer("👨‍👩‍👧‍👦 Ваше семейное положение:", reply_markup=hammasi_rus)
        await rus_state.next()
    else:
        await message.answer("Вы ввели номер телефона в неправильном формате. Пожалуйста, введите номер еще раз (+998XXXXXXXXX в формате).", reply_markup=hammasi_rus)

@dp.message_handler(state=rus_state.oilaviy_ahvol)
async def answer_lavozim(message: types.Message, state: FSMContext):
    oila = message.text
    await state.update_data({"Семейное положение": oila})
    await message.answer("Выберите ваш уровень образования:", reply_markup=mall_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.malumot)
async def answer_lavozim(message: types.Message, state: FSMContext):
    malumoti = message.text
    await state.update_data({"malumoti": malumoti})
    await message.answer("Вы когда-нибудь работали в нашей компании?:", reply_markup=komp_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.avval_kompdaishlagan)
async def answer_lavozim(message: types.Message, state: FSMContext):
    kompp = message.text
    await state.update_data({"Работали ли вы": kompp})
    await message.answer("Выберите размер корпоративной формы (футболка, рубашка):", reply_markup=mayka_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.mayka)
async def answer_lavozim(message: types.Message, state: FSMContext):
    mayka = message.text
    await state.update_data({"Форма": mayka})
    await message.answer("Вы студент, школьник или колледжант?", reply_markup=komp_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.oqiydi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    oqiydi = message.text
    await state.update_data({"Учились ли вы": oqiydi})
    await message.answer("Какой у вас вид обучения?", reply_markup=talim_shakli_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.talim_shakli)
async def answer_lavozim(message: types.Message, state: FSMContext):
    talim_shakli = message.text
    await state.update_data({"Вид обучения": talim_shakli})
    await message.answer("""◀️🏦 Где, когда и кем вы работали. Опишите работы, которые имеют 
    значение для 3-4 места. Ваш опыт работы является важным для нас.\n\nНапример, рекрутер в магазинах "kometa" в 2020-2022 годах""", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.kim_bolishishlagan)
async def answer_lavozim(message: types.Message, state: FSMContext):
    kim_bolishishlagan = message.text
    await state.update_data({"Кем работали": kim_bolishishlagan})
    await message.answer("👨‍💻 Какие программы на компьютере вы знаете? (Excel, Word, Power Point)", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.kompyuterda_nmbiladi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    kompyuterda_nmbiladi = message.text
    await state.update_data({"Компьютер": kompyuterda_nmbiladi})
    await message.answer("Какую зарплату вы хотите получить?", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.oylik)
async def answer_lavozim(message: types.Message, state: FSMContext):
    oylik = message.text
    await state.update_data({"Зарплата": oylik})
    await message.answer("""❗️У вас есть близкие родственники, работающие в компании "kometa"? Если да, то напишите его полное имя, имя отца и его должность:""", reply_markup=yoq_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.yaqin_odam)
async def answer_lavozim(message: types.Message, state: FSMContext):
    yaqin_odam = message.text
    await state.update_data({"Близкий родственник": yaqin_odam})
    await message.answer("Вы гражданин Республики Узбекистан?", reply_markup=komp_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.ozbek_fuqorasimi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    ozbek_fuqorasimi = message.text
    await state.update_data({"Гражданин Узбекистана": ozbek_fuqorasimi})
    await message.answer("Вы сейчас находитесь на работе?", reply_markup=komp_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.ishlaysizmi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    ishlaysizmi = message.text
    await state.update_data({"Вы работаете": ishlaysizmi})
    await message.answer("Где вы узнали о вакансии?", reply_markup=ishorin_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.ish_qayerdanbildiz)
async def answer_lavozim(message: types.Message, state: FSMContext):
    ish_qayerdanbildiz = message.text
    await state.update_data({"Откуда вы узнали о работе": ish_qayerdanbildiz})
    await message.answer("📷 Прикрепите свою фотографию:", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.rasm, content_types=['photo'])
async def answer_rasm(message: types.Message, state: FSMContext):
    photo = message.photo[-1]  # Берем самое качественное фото
    photo_id = photo.file_id
    await state.update_data({"Фото": photo_id})
    await message.answer("Сколько языков вы знаете?", reply_markup=hammasi_rus)
    await rus_state.next()

@dp.message_handler(state=rus_state.til_bilish)
async def answer_til_bilish(message: types.Message, state: FSMContext):
    til = message.text
    if til.isdigit():
        await state.update_data({"Количество изучаемых языков": til})

        data = await state.get_data()
        fullname = data.get("ФИО")
        date = data.get("Дата рождения")
        viloyat = data.get("Вилойат")
        tuman = data.get("Туман")
        kasb = data.get("Профессия")
        jins = data.get("Пол")
        mutaxasisligi = data.get("Специализация")
        lavozim = data.get("Должность")
        tajriba = data.get("Опыт")
        raqam = data.get("Номер телефона")
        til = data.get("Количество изучаемых языков")
        oilaviy_ahvoli = data.get("Семейное положение")
        ma_lumoti = data.get("malumoti")
        ishlaganmi = data.get("Работали ли вы")
        mayka = data.get("Форма")
        o_qiydimi = data.get("Учились ли вы")
        talim = data.get("Вид обучения")
        ishni_qayerdan_bildiz = data.get("Откуда вы узнали о работе")
        rasm = data.get("Фото")
        kompyuterda_nmbiladi = data.get("Кем работали")

        msg = (
            "✅ Приняты следующие данные:\n"
            f"👤 Имя - {fullname}\n"
            f"🎂 Дата рождения - {date}\n"   
            f"🏠 Вилойат - {viloyat}\n"
            f"🏡 Туман - {tuman}\n"
            f"👨‍🔧 Профессия - {kasb}\n"
            f"👤 Пол - {jins}\n"
            f"🎓 Специализация - {mutaxasisligi}\n"
            f"💼 Должность - {lavozim}\n"
            f"📅 Опыт работы - {tajriba}\n"
            f"📱 Телефонный номер - {raqam}\n"
            f"🔤 Количество изучаемых языков - {til}\n"
            f"👨‍👩‍👧‍👦 Семейное положение - {oilaviy_ahvoli}\n"
            f"🎓 Образование - {ma_lumoti}\n"
            f"💼 Работали ли - {ishlaganmi}\n"
            f"👕 Размер одежды - {mayka}\n"
            f"📚 Учитесь ли вы - {o_qiydimi}\n"
            f"🎓 Форма обучения - {talim}\n"
            f"🏢 Где, когда и кем работали ранее - {ishni_qayerdan_bildiz}\n"
            f"🖼️ Фото - {rasm}\n"
            f"💻 Компьютерные программы - {kompyuterda_nmbiladi}\n"
        )

        await message.answer(msg)
        await message.answer("Все данные приняты?", reply_markup=check_rus)
        await rus_state.next()
    else:
        await message.answer("Пожалуйста, введите в правильном формате. Введите только числа.", reply_markup=hammasi_rus)

@dp.message_handler(state=rus_state.tekshirish)
async def check(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        data = await state.get_data()

        rasm = data.get("Фото")
        if rasm:
            await bot.send_photo(chat_id=1130279498, photo=rasm)
        else:
            await message.reply("Никакие фотографии не сохранены.")

        fullname = data.get("ФИО")
        date = data.get("Дата рождения")
        viloyat = data.get("Вилойат")
        tuman = data.get("Туман")
        kasb = data.get("Профессия")
        jins = data.get("Пол")
        mutaxasisligi = data.get("Специализация")
        lavozim = data.get("Должность")
        tajriba = data.get("Опыт")
        raqam = data.get("Номер телефона")
        til = data.get("Количество изучаемых языков")
        oilaviy_ahvoli = data.get("Семейное положение")
        ma_lumoti = data.get("malumoti")
        ishlaganmi = data.get("Работали ли вы")
        mayka = data.get("Форма")
        o_qiydimi = data.get("Учились ли вы")
        talim = data.get("Вид обучения")
        ishni_qayerdan_bildiz = data.get("Откуда вы узнали о работе")
        rasm = data.get("Фото")
        kompyuterda_nmbiladi = data.get("Кем работали")

        msg = (
            "✅ Приняты следующие данные:\n"
            f"👤 Имя - {fullname}\n"
            f"🎂 Дата рождения - {date}\n"
            f"🏠 Вилойат - {viloyat}\n"
            f"🏡 Туман - {tuman}\n"
            f"👨‍🔧 Профессия - {kasb}\n"
            f"👤 Пол - {jins}\n"
            f"🎓 Специализация - {mutaxasisligi}\n"
            f"💼 Должность - {lavozim}\n"
            f"📅 Опыт работы - {tajriba}\n"
            f"📱 Телефонный номер - {raqam}\n"
            f"🔤 Количество изучаемых языков - {til}\n"
            f"👨‍👩‍👧‍👦 Семейное положение - {oilaviy_ahvoli}\n"
            f"🎓 Образование - {ma_lumoti}\n"
            f"💼 Работали ли - {ishlaganmi}\n"
            f"👕 Размер одежды - {mayka}\n"
            f"📚 Учитесь ли вы - {o_qiydimi}\n"
            f"🎓 Форма обучения - {talim}\n"
            f"🏢 Где, когда и кем работали ранее - {ishni_qayerdan_bildiz}\n"
            f"🖼️ Фото - {rasm}\n"
            f"💻 Компьютерные программы - {kompyuterda_nmbiladi}\n"
        )

        await bot.send_message(chat_id=1130279498, text=msg)
        await message.answer("Информация получена. Мы свяжемся с вами в ближайшее время.", reply_markup=bosh_menu)
        await state.finish()
    else:
        await message.answer("Не принимаются", reply_markup=bosh_menu)
        await state.finish()
