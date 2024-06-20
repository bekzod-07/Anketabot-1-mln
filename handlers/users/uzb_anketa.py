from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime

from keyboards.default.Menu import bosh_menu
from keyboards.default.chek import chek
from keyboards.default.hammasi import hammasi_uz
from keyboards.default.ishorin import ishorin
from keyboards.default.jins import jinss
from keyboards.default.komppp import komp
from keyboards.default.mayka import mayka
from keyboards.default.talim_shakli import talim_shakli
from keyboards.default.til import til
from keyboards.default.tuman import tum
from keyboards.default.viloyat import vil
from keyboards.default.oilasi import oil
from keyboards.default.mal import mall
from keyboards.default.yoq import yoq
from keyboards.default.ish import ish_uz
from loader import dp, bot
from states.uzb_state import uzb_state

from aiogram.dispatcher.filters import Text

valid_viloyatlar = ["Buxoro viloyati"]
valid_tumanlar = ["Shofirkon tumani", "Romitan tumani"]

@dp.message_handler(Text(equals="Bekor qilish 🚫"), state='*')
async def cancel_action(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Kerakli menu tanlang", reply_markup=bosh_menu)

@dp.message_handler(text="Anketa to'ldirish 📝")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! ✨", reply_markup=til)

@dp.message_handler(text="🇺🇿 O'zbek tili 🇺🇿", state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting\n\nFIO(Gafurov Lochinbek Faxriddin oʻgʻli) formatida: 📋", reply_markup=hammasi_uz)
    await uzb_state.fio.set()

@dp.message_handler(state=uzb_state.fio)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"FIO": fullname})
    await message.answer("📅 Tug‘ilgan sanangiz :\n\nKK.OO.YYYY (15.10.2007) formatida:", reply_markup=hammasi_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.date)
async def answer_date(message: types.Message, state: FSMContext):
    date_str = message.text
    try:
        date = datetime.strptime(date_str, "%d.%m.%Y")

        if date.year > 2024:
            await message.answer("Sizning tug'ilgan sanangizning yili 2024 dan katta bo'lishi mumkin emas.", reply_markup=hammasi_uz)
        else:
            await state.update_data({"Date": date_str})
            await message.answer("Viloyatini tanlang", reply_markup=vil)
            await uzb_state.next()
    except ValueError:
        await message.answer("Iltimos, tug'ilgan sanani to'g'ri formatda kiriting (KK.OO.YYYY).", reply_markup=hammasi_uz)


@dp.message_handler(state=uzb_state.viloyat)
async def answer_viloyat(message: types.Message, state: FSMContext):
    viloyat = message.text
    if viloyat in valid_viloyatlar:
        await state.update_data({"Viloyat": viloyat})
        await message.answer("Tumani tanlang", reply_markup=tum)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, viloyatni ro'yxatdagi tugmalardan tanlang.", reply_markup=vil)

@dp.message_handler(state=uzb_state.tuman)
async def answer_tuman(message: types.Message, state: FSMContext):
    tuman = message.text
    if tuman in valid_tumanlar:
        await state.update_data({"Tuman": tuman})
        await message.answer("Kasbingizni kiriting", reply_markup=hammasi_uz)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, tumanni ro'yxatdagi tugmalardan tanlang.")

@dp.message_handler(state=uzb_state.kasbi)
async def answer_kasb(message: types.Message, state: FSMContext):
    kasb = message.text
    await state.update_data({"Kasbi": kasb})
    await message.answer("Jinsingizni tanlang", reply_markup=jinss)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.jinsi)
async def answer_jins(message: types.Message, state: FSMContext):
    jins = message.text
    if jins in ["Erkak", "Ayol"]:
        await state.update_data({"Jinsi": jins})
        await message.answer("Mutaxasisligingiz nima", reply_markup=hammasi_uz)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, jinsni ro'yxatdagi tugmalardan tanlang.", reply_markup=jinss)


@dp.message_handler(state=uzb_state.mutaxasislik)
async def answer_mutaxasislik(message: types.Message, state: FSMContext):
    mutaxasisligi = message.text
    await state.update_data({"Mutaxasisligi": mutaxasisligi})
    await message.answer("Qanday lavozimga ishlamoqchisiz", reply_markup=ish_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.ishlash_lavozimi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    lavozim = message.text
    if lavozim in ["Sotuvchi", "Qoʻriqlash xizmati", "Kassir", "Haydovchi", "Novoy", "Operator"]:
        await state.update_data({"Lavozimi": lavozim})
        await message.answer("Necha yil tajribaga egasiz", reply_markup=hammasi_uz)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, tanlangan variantlar ichidan birini tanlang.")

@dp.message_handler(state=uzb_state.ish_tajriba)
async def answer_tajriba(message: types.Message, state: FSMContext):
    tajriba = message.text
    if tajriba.isdigit() and int(tajriba) <= 50:
        await state.update_data({"Tajriba": tajriba})
        await message.answer("Telefon raqamizni yozing", reply_markup=hammasi_uz)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, 50 dan ko'p bo'lmagan raqam kiriting.", reply_markup=hammasi_uz)


@dp.message_handler(state=uzb_state.tele_raqam)
async def answer_raqam(message: types.Message, state: FSMContext):
    raqam = message.text
    if raqam.startswith("+998") and len(raqam) == 13 and raqam[1:].isdigit():
        await state.update_data({"Telefon raqam": raqam})
        await message.answer("👨‍👩‍👧‍👦 Oilaviy ahvolingiz:", reply_markup=oil)
        await uzb_state.next()
    else:
        await message.answer("Telefon raqamni noto'g'ri formatda kiritdingiz. Iltimos, raqamni qayta kiriting (+998XXXXXXXXX formatida).", reply_markup=hammasi_uz)

@dp.message_handler(state=uzb_state.oilaviy_ahvol)
async def answer_lavozim(message: types.Message, state: FSMContext):
    oila = message.text
    await state.update_data({"Oilaviy ahvoli": oila})
    await message.answer("Maʼlumotingizni tanlang:", reply_markup=mall)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.malumot)
async def answer_lavozim(message: types.Message, state: FSMContext):
    malumoti = message.text
    await state.update_data({"Malumoti nima": malumoti})
    await message.answer("Siz avval bizning kompaniyamizda ishlaganmisiz?:", reply_markup=komp)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.avval_kompdaishlagan)
async def answer_lavozim(message: types.Message, state: FSMContext):
    kompp = message.text
    await state.update_data({"Ishlaganmi": kompp})
    await message.answer("Korporativ forma olish uchun kiyimingizning o'lchamini tanlang (futbolka, ko'ylak):", reply_markup=mayka)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.mayka)
async def answer_lavozim(message: types.Message, state: FSMContext):
    mayka = message.text
    await state.update_data({"Mayka": mayka})
    await message.answer("Siz hozirda qaysidir universitet, litsey yoki kollej talabasimisiz?", reply_markup=komp)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.oqiydi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    oqiydi = message.text
    await state.update_data({"O'qiydimi": oqiydi})
    await message.answer("Qanday ta'lim shakli?", reply_markup=talim_shakli)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.talim_shakli)
async def answer_lavozim(message: types.Message, state: FSMContext):
    talim_shakli = message.text
    await state.update_data({"Talim": talim_shakli})
    await message.answer("""◀️🏦 Qayerda, qachon va kim bo'lib ishlaganingizni ayting. 3-4 o'rin uchun ahamiyatli bo'lgan ishlarni tavsiflang. Sizning rasmiy va norasmiy ish tajribangiz biz uchun muhim.\n\nMisol uchun, 2020-2022 yillarda "Kometa" do'konlar tarmog'ida rekruter""", reply_markup=hammasi_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.kim_bolishishlagan)
async def answer_lavozim(message: types.Message, state: FSMContext):
    kim_bolishishlagan = message.text
    await state.update_data({"Kim bo'lib ishlagan": kim_bolishishlagan})
    await message.answer("👨‍💻 Kompyuterda qaysi dasturlardan foydalana olasiz?(Excel, Word, Power Point)", reply_markup=hammasi_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.kompyuterda_nmbiladi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    kompyuterda_nmbiladi = message.text
    await state.update_data({"Kompyuter": kompyuterda_nmbiladi})
    await message.answer("Qancha Oylik olishni istaysiz?", reply_markup=hammasi_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.oylik)
async def answer_oylik(message: types.Message, state: FSMContext):
    oylik = message.text
    if oylik.isdigit():
        await state.update_data({"Oylik": oylik})
        await message.answer("""❗️"Kometa" kompaniyasida ishlaydigan yaqin 
qarindoshlaringiz bormi? Agar bo'lsa, to'liq familiyasi, ismi, otasining ismini va lavozimini yozing:""", reply_markup=yoq)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, qancha oylik olishni istashingizni raqam bilan kiriting.")

@dp.message_handler(state=uzb_state.yaqin_odam)
async def answer_lavozim(message: types.Message, state: FSMContext):
    yaqin_odam = message.text
    await state.update_data({"Yaqin qarindoshi": yaqin_odam})
    await message.answer("Siz O'zbekiston Respublikasi fuqarosimisiz?", reply_markup=komp)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.ozbek_fuqorasimi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    ozbek_fuqorasimi = message.text
    await state.update_data({"Ozbek fuqorasimi": ozbek_fuqorasimi})
    await message.answer("Siz hozirda ish bilan ta'minlanganmisiz?", reply_markup=komp)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.ishlaysizmi)
async def answer_lavozim(message: types.Message, state: FSMContext):
    ishlaysizmi = message.text
    await state.update_data({"Ishlaysizmi": ishlaysizmi})
    await message.answer("Bo'sh ish o'rni haqida qayerdan bildingiz?", reply_markup=ishorin)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.ish_qayerdanbildiz)
async def answer_lavozim(message: types.Message, state: FSMContext):
    ish_qayerdanbildiz = message.text
    await state.update_data({"Ishni qayerdan bildiz": ish_qayerdanbildiz})
    await message.answer("📷 O‘zingizni rasmingizni yuboring:", reply_markup=hammasi_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.rasm, content_types=['photo'])
async def answer_rasm(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    photo_id = photo.file_id
    await state.update_data({"Rasm": photo_id})
    await message.answer("Nechta tilini bilasiz?", reply_markup=hammasi_uz)
    await uzb_state.next()

@dp.message_handler(state=uzb_state.rasm)
async def handle_invalid_content(message: types.Message):
    if message.content_type == 'photo':
        await message.answer("Rasm yuborilishi kerak. Iltimos, rasmni yuboring:", reply_markup=hammasi_uz)
    else:
        await message.answer("Rasm yuborilishi kerak. Iltimos, faqat rasmni yuboring:", reply_markup=hammasi_uz)

@dp.message_handler(state=uzb_state.til_bilish)
async def answer_til_bilish(message: types.Message, state: FSMContext):
    til = message.text
    if til.isdigit():
        await state.update_data({"Nechta tilini biladi": til})

        data = await state.get_data()
        fullname = data.get("FIO")
        date = data.get("Date")
        viloyat = data.get("Viloyat")
        tuman = data.get("Tuman")
        kasb = data.get("Kasbi")
        jins = data.get("Jinsi")
        mutaxasisligi = data.get("Mutaxasisligi")
        lavozim = data.get("Lavozimi")
        tajriba = data.get("Tajriba")
        raqam = data.get("Telefon raqam")
        til = data.get("Nechta tilini biladi")
        oilaviy_ahvoli = data.get("Oilaviy ahvoli")
        malumoti = data.get("Malumoti nima")
        ishlaganmi = data.get("Ishlaganmi")
        mayka = data.get("Mayka")
        o_qiydimi = data.get("O'qiydimi")
        talim = data.get("Talim")
        ishni_qayerdan_bildiz = data.get("Ishni qayerdan bildiz")
        rasm = data.get("Rasm")
        kompyuterda_nmbiladi = data.get("Kompyuter")

        msg = (
            "✅ Quyidagi ma'lumotlar qabul qilindi:\n"
            f"👤 Ismi - {fullname}\n"
            f"🎂 Tug‘ilgan sana - {date}\n"
            f"🏠 Viloyati - {viloyat}\n"
            f"🏡 Tumani - {tuman}\n"
            f"👨‍🔧 Kasbi - {kasb}\n"
            f"👤 Jinsi - {jins}\n"
            f"🎓 Mutaxasisligi - {mutaxasisligi}\n"
            f"💼 Lavozim - {lavozim}\n"
            f"📅 Tajriba - {tajriba}\n"
            f"📱 Telefon raqam - {raqam}\n"
            f"🔤 Nechta tilini biladi - {til}\n"
            f"👨‍👩‍👧‍👦 Oilaviy ahvoli - {oilaviy_ahvoli}\n"
            f"🎓 Ma'lumoti - {malumoti}\n"
            f"💼 Ishlaganmi - {ishlaganmi}\n"
            f"👕 Mayka - {mayka}\n"
            f"📚 O'qiydimi - {o_qiydimi}\n"
            f"🎓 Talim shakli - {talim}\n"
            f"🏢 Ishni qayerdan bildiz - {ishni_qayerdan_bildiz}\n"
            f"🖼️ Rasm - {rasm}\n"
            f"💻 Kompyuterda qanday dasturlar biladi - {kompyuterda_nmbiladi}\n"
        )
        await message.answer(msg)
        await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=chek)
        await uzb_state.next()
    else:
        await message.answer("Iltimos, to'g'ri formatda kiriting. Faqat raqam kiriting.", reply_markup=hammasi_uz)

@dp.message_handler(state=uzb_state.tekshirish)
async def chesk(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()
        rasm = data.get("Rasm")
        if rasm:
            fullname = data.get("FIO")
            date = data.get("Date")
            viloyat = data.get("Viloyat")
            tuman = data.get("Tuman")
            kasb = data.get("Kasbi")
            jins = data.get("Jinsi")
            mutaxasisligi = data.get("Mutaxasisligi")
            lavozim = data.get("Lavozimi")
            tajriba = data.get("Tajriba")
            raqam = data.get("Telefon raqam")
            til = data.get("Nechta tilini biladi")
            oilaviy_ahvoli = data.get("Oilaviy ahvoli")
            malumoti = data.get("Malumoti nima")
            ishlaganmi = data.get("Ishlaganmi")
            mayka = data.get("Mayka")
            o_qiydimi = data.get("O'qiydimi")
            talim = data.get("Talim")
            ishni_qayerdan_bildiz = data.get("Ishni qayerdan bildiz")
            kompyuterda_nmbiladi = data.get("Kompyuter")

            caption = (
                "✅ Quyidagi ma'lumotlar qabul qilindi:\n"
                f"👤 Ismi - {fullname}\n"
                f"🎂 Tug‘ilgan sana - {date}\n"
                f"🏠 Viloyati - {viloyat}\n"
                f"🏡 Tumani - {tuman}\n"
                f"👨‍🔧 Kasbi - {kasb}\n"
                f"👤 Jinsi - {jins}\n"
                f"🎓 Mutaxasisligi - {mutaxasisligi}\n"
                f"💼 Lavozim - {lavozim}\n"
                f"📅 Tajriba - {tajriba}\n"
                f"📱 Telefon raqam - {raqam}\n"
                f"🔤 Nechta tilini biladi - {til}\n"
                f"👨‍👩‍👧‍👦 Oilaviy ahvoli - {oilaviy_ahvoli}\n"
                f"🎓 Ma'lumoti - {malumoti}\n"
                f"💼 Ishlaganmi - {ishlaganmi}\n"
                f"👕 Mayka - {mayka}\n"
                f"📚 O'qiydimi - {o_qiydimi}\n"
                f"🎓 Talim shakli - {talim}\n"
                f"🏢 Ishni qayerdan bildiz - {ishni_qayerdan_bildiz}\n"
                f"💻 Kompyuterda qanday dasturlar biladi - {kompyuterda_nmbiladi}\n"
            )

            await bot.send_photo(chat_id=1130279498, photo=rasm, caption=caption)
            await message.answer("Ma'lumotlar qabul qilindi. Tez orada siz bilan bog'lanamiz.", reply_markup=bosh_menu)
            await state.finish()
        else:
            await message.reply("Hech qanday rasm saqlanmagan.")
    else:
        await message.answer("Qabul qilinmadi", reply_markup=bosh_menu)
        await state.finish()
