from aiogram.dispatcher.filters import Text

from aiogram import types
from aiogram.dispatcher import FSMContext
from datetime import datetime

from keyboards.default.Menu import bosh_menu
from keyboards.default.chek import check
from keyboards.default.hammasi import hammasi_eng
from keyboards.default.ishorin import ishorin_eng
from keyboards.default.jins import jinss_eng
from keyboards.default.komppp import komp, komp_eng
from keyboards.default.mayka import mayka_eng
from keyboards.default.talim_shakli import talim_shakli_eng
from keyboards.default.tuman import tum_eng
from keyboards.default.viloyat import vil_eng
from keyboards.default.yoq import yoq_eng
from keyboards.default.ish import ish_rus
from loader import dp, bot
from states.eng_state import eng_state

@dp.message_handler(Text(equals="Cancle 🚫"), state='*')
async def cancel_action(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Select the desired menu", reply_markup=bosh_menu)

@dp.message_handler(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English language 🏴󠁧󠁢󠁥󠁮󠁧󠁿")
async def enter_test(message: types.Message):
    await message.answer("Please enter your full name\n\nIn the format:Gafurov Lochinbek Fakhriddin 📋", reply_markup=hammasi_eng)
    await eng_state.full_name.set()

valid_regions = ["Bukhara region"]
valid_districts = ["Shafirkan district", "Romitan district"]

@dp.message_handler(state=eng_state.full_name)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"Full name": fullname})
    await message.answer("📅 Date of birth :\n\nDD.MM.YYYY (15.10.2007) format:", reply_markup=hammasi_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.date_of_birth)
async def answer_date(message: types.Message, state: FSMContext):
    date_str = message.text
    try:
        date = datetime.strptime(date_str, "%d.%m.%Y")
        if date.year > 2024:
            await message.answer("The year of your birth cannot be later than 2024.", reply_markup=hammasi_eng)
        else:
            await state.update_data({"Date": date_str})
            await message.answer("Select your region", reply_markup=vil_eng)
            await eng_state.next()
    except ValueError:
        await message.answer("Please enter the date of birth in the correct format (DD.MM.YYYY).", reply_markup=hammasi_eng)

@dp.message_handler(state=eng_state.region)
async def answer_region(message: types.Message, state: FSMContext):
    region = message.text
    if region in valid_regions:
        await state.update_data({"Region": region})
        await message.answer("Select your district", reply_markup=tum_eng)
        await eng_state.next()
    else:
        await message.answer("Please select the region from the listed buttons.", reply_markup=vil_eng)

@dp.message_handler(state=eng_state.district)
async def answer_district(message: types.Message, state: FSMContext):
    district = message.text
    if district in valid_districts:
        await state.update_data({"District": district})
        await message.answer("Enter your occupation", reply_markup=hammasi_eng)
        await eng_state.next()
    else:
        await message.answer("Please select the district from the listed buttons.")

@dp.message_handler(state=eng_state.occupation)
async def answer_occupation(message: types.Message, state: FSMContext):
    occupation = message.text
    await state.update_data({"Occupation": occupation})
    await message.answer("Select your gender", reply_markup=jinss_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.gender)
async def answer_gender(message: types.Message, state: FSMContext):
    gender = message.text
    if gender in ["Male", "Female"]:
        await state.update_data({"Gender": gender})
        await message.answer("What is your specialization", reply_markup=hammasi_eng)
        await eng_state.next()
    else:
        await message.answer("Please select the gender from the listed buttons.", reply_markup=jinss_eng)

@dp.message_handler(state=eng_state.specialization)
async def answer_specialization(message: types.Message, state: FSMContext):
    specialization = message.text
    await state.update_data({"Specialization": specialization})
    await message.answer("What position do you want to work in?", reply_markup=hammasi_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.position)
async def answer_position(message: types.Message, state: FSMContext):
    position = message.text
    await state.update_data({"Position": position})
    await message.answer("How many years of experience do you have?", reply_markup=ish_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.experience)
async def answer_experience(message: types.Message, state: FSMContext):
    experience = message.text
    if experience.isdigit():
        await state.update_data({"Experience": experience})
        await message.answer("Enter your phone number", reply_markup=hammasi_eng)
        await eng_state.next()
    else:
        await message.answer("Please enter only numbers.", reply_markup=hammasi_eng)

@dp.message_handler(state=eng_state.phone_number)
async def answer_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    if phone_number.startswith("+998") and len(phone_number) == 13 and phone_number[1:].isdigit():
        await state.update_data({"Phone number": phone_number})
        await message.answer("👩‍👧‍👦 Your marital status:", reply_markup=hammasi_eng)
        await eng_state.next()
    else:
        await message.answer("You entered the phone number in the wrong format. Please enter the number again (+998XXXXXXXXX format).", reply_markup=hammasi_eng)

@dp.message_handler(state=eng_state.marital_status)
async def answer_position(message: types.Message, state: FSMContext):
    family_status = message.text
    await state.update_data({"Family Status": family_status})
    await message.answer("Please select your education level:", reply_markup=talim_shakli_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.information)
async def answer_position(message: types.Message, state: FSMContext):
    education_level = message.text
    await state.update_data({"Education Level": education_level})
    await message.answer("Have you worked with our company before?", reply_markup=yoq_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.previously_employed)
async def answer_position(message: types.Message, state: FSMContext):
    worked_before = message.text
    await state.update_data({"Worked Before": worked_before})
    await message.answer("Choose the size of corporate clothing (t-shirt, jacket) for uniform:", reply_markup=mayka_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.size_of_uniform)
async def answer_position(message: types.Message, state: FSMContext):
    uniform_size = message.text
    await state.update_data({"Uniform Size": uniform_size})
    await message.answer("What is your current educational institution (university, lyceum, or college)?", reply_markup=komp_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.attending_school)
async def answer_position(message: types.Message, state: FSMContext):
    attending_school = message.text
    await state.update_data({"Attending School": attending_school})
    await message.answer("What is your learning style?", reply_markup=talim_shakli_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.learning_style)
async def answer_position(message: types.Message, state: FSMContext):
    learning_style = message.text
    await state.update_data({"Learning Style": learning_style})
    await message.answer("""◀️🏦 Describe where, when, and who you worked for. Describe the 
    most important tasks for 3-4 places. Your official and non-official work experience is important to us.\n\nFor example, 
    recruiter at "kometa" store chain from 2020 to 2022""", reply_markup=hammasi_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.workplace)
async def answer_position(message: types.Message, state: FSMContext):
    working_place = message.text
    await state.update_data({"Working Place": working_place})
    await message.answer("👨‍💻 What computer programs can you use? (Excel, Word, Power Point)", reply_markup=hammasi_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.computer_skills)
async def answer_position(message: types.Message, state: FSMContext):
    computer_skills = message.text
    await state.update_data({"Computer Skills": computer_skills})
    await message.answer("What is your desired monthly salary?", reply_markup=hammasi_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.desired_salary)
async def answer_position(message: types.Message, state: FSMContext):
    desired_salary = message.text
    await state.update_data({"Desired Salary": desired_salary})
    await message.answer("""❗️Do you have any close relatives working at the "kometa" company? If so, please write 
    their full name, family name, father's name, and position:""", reply_markup=yoq_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.close_relative)
async def answer_position(message: types.Message, state: FSMContext):
    close_relatives = message.text
    await state.update_data({"Close Relatives": close_relatives})
    await message.answer("Are you a citizen of the Republic of Uzbekistan?", reply_markup=komp_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.uzbek_citizen)
async def answer_position(message: types.Message, state: FSMContext):
    uzbek_citizen = message.text
    await state.update_data({"Uzbek Citizen": uzbek_citizen})
    await message.answer("Are you currently employed?", reply_markup=komp_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.employed)
async def answer_position(message: types.Message, state: FSMContext):
    employed = message.text
    await state.update_data({"Employed": employed})
    await message.answer("Where did you hear about the vacant position?", reply_markup=ishorin_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.job_origin)
async def answer_position(message: types.Message, state: FSMContext):
    job_source = message.text
    await state.update_data({"Job Source": job_source})
    await message.answer("📷 Upload your photo:", reply_markup=hammasi_eng)
    await eng_state.next()

@dp.message_handler(state=eng_state.photo, content_types=['photo'])
async def answer_photo(message: types.Message, state: FSMContext):
    photo = message.photo[-1]  # Get the highest quality photo
    photo_id = photo.file_id
    await state.update_data({"Photo": photo_id})
    await message.answer("How many languages do you speak?", reply_markup=hammasi_eng)
    await eng_state.next()


@dp.message_handler(state=eng_state.language_proficiency)
async def answer_language_proficiency(message: types.Message, state: FSMContext):
    languages = message.text
    if languages.isdigit():
        await state.update_data({"Number of Languages": languages})

        data = await state.get_data()
        fullname = data.get("Full name")
        date_of_birth = data.get("Date")
        region = data.get("Region")
        district = data.get("District")
        occupation = data.get("Occupation")
        gender = data.get("Gender")
        specialization = data.get("Specialization")
        position = data.get("Position")
        experience = data.get("Experience")
        phone_number = data.get("Phone Number")
        languages = data.get("Number of Languages")
        family_status = data.get("Family Status")
        education_level = data.get("Education Level")
        worked_before = data.get("Worked Before")
        uniform_size = data.get("Uniform Size")
        attending_school = data.get("Attending School")
        learning_style = data.get("Learning Style")
        working_place = data.get("Working Place")
        computer_skills = data.get("Computer Skills")
        desired_salary = data.get("Desired Salary")
        close_relatives = data.get("Close Relatives")
        uzbek_citizen = data.get("Uzbek Citizen")
        employed = data.get("Employed")
        job_source = data.get("Job Source")
        photo = data.get("Photo")

        msg = (
            "✅ The following information has been received:\n"
            f"👤 Full Name - {fullname}\n"
            f"🎂 Date of Birth - {date_of_birth}\n"
            f"🏠 Region - {region}\n"
            f"🏡 District - {district}\n"
            f"👨‍🔧 Occupation - {occupation}\n"
            f"👤 Gender - {gender}\n"
            f"🎓 Specialization - {specialization}\n"
            f"💼 Position - {position}\n"
            f"📅 Experience - {experience}\n"
            f"📱 Phone Number - {phone_number}\n"
            f"🔤 Number of Languages - {languages}\n"
            f"👨‍👩‍👧‍👦 Family Status - {family_status}\n"
            f"🎓 Education Level - {education_level}\n"
            f"💼 Worked Before - {worked_before}\n"
            f"👕 Uniform Size - {uniform_size}\n"
            f"📚 Attending School - {attending_school}\n"
            f"🎓 Learning Style - {learning_style}\n"
            f"🏢 Working Place - {working_place}\n"
            f"💻 Computer Skills - {computer_skills}\n"
            f"💰 Desired Salary - {desired_salary}\n"
            f"👨‍👩‍👧‍👦 Close Relatives - {close_relatives}\n"
            f"🌍 Uzbek Citizen - {uzbek_citizen}\n"
            f"🏢 Employed - {employed}\n"
            f"📖 Job Source - {job_source}\n"
            f"🖼️ Photo - {photo}\n"
        )

        await message.answer(msg)
        await message.answer("Are all the details correct?", reply_markup=check)
        await eng_state.next()
    else:
        await message.answer("Please enter a valid number. Only digits are allowed.", reply_markup=hammasi_eng)

@dp.message_handler(state=eng_state.check_details)
async def check_details(message: types.Message, state: FSMContext):
    if message.text.lower() == "yes":
        data = await state.get_data()

        photo = data.get("Photo")
        if photo:
            await bot.send_photo(chat_id=1130279498, photo=photo)
        else:
            await message.reply("No photo has been saved.")

        fullname = data.get("Full name")
        date_of_birth = data.get("Date")
        region = data.get("Region")
        district = data.get("District")
        occupation = data.get("Occupation")
        gender = data.get("Gender")
        specialization = data.get("Specialization")
        position = data.get("Position")
        experience = data.get("Experience")
        phone_number = data.get("Phone Number")
        languages = data.get("Number of Languages")
        family_status = data.get("Family Status")
        education_level = data.get("Education Level")
        worked_before = data.get("Worked Before")
        uniform_size = data.get("Uniform Size")
        attending_school = data.get("Attending School")
        learning_style = data.get("Learning Style")
        working_place = data.get("Working Place")
        computer_skills = data.get("Computer Skills")

        msg = (
            "✅ The following information has been received:\n"
            f"👤 Full Name - {fullname}\n"
            f"🎂 Date of Birth - {date_of_birth}\n"
            f"🏠 Region - {region}\n"
            f"🏡 District - {district}\n"
            f"👨‍🔧 Occupation - {occupation}\n"
            f"👤 Gender - {gender}\n"
            f"🎓 Specialization - {specialization}\n"
            f"💼 Position - {position}\n"
            f"📅 Experience - {experience}\n"
            f"📱 Phone Number - {phone_number}\n"
            f"🔤 Number of Languages - {languages}\n"
            f"👨‍👩‍👧‍👦 Family Status - {family_status}\n"
            f"🎓 Education Level - {education_level}\n"
            f"💼 Worked Before - {worked_before}\n"
            f"👕 Uniform Size - {uniform_size}\n"
            f"📚 Attending School - {attending_school}\n"
            f"🎓 Learning Style - {learning_style}\n"
            f"🏢 Working Place - {working_place}\n"
            f"💻 Computer Skills - {computer_skills}\n"
        )

        await bot.send_message(chat_id=1130279498, text=msg)
        await message.answer("The information has been received. We will contact you shortly.", reply_markup=bosh_menu)
        await state.finish()
    else:
        await message.answer("Not accepted", reply_markup=bosh_menu)
        await state.finish()
