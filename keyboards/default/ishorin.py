from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ishorin = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Ish qidirish uchun telegram kanali"),
            KeyboardButton(text="Olx.uz")
        ],
        [
            KeyboardButton(text="hh.uz"),
            KeyboardButton(text="ishonchsavdo.uz")
        ],
        [
            KeyboardButton(text="banner(ko'chadagi reklama)"),
            KeyboardButton(text="flayer")
        ],
        [
            KeyboardButton(text="Tanish / qarindoshi / do'stim aytdi"),
            KeyboardButton(text="Bekor qilish 🚫")
        ],

    ],
    resize_keyboard=True
)

ishorin_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Канал для поиска работы в Telegram"),
            KeyboardButton(text="Olx.uz")
        ],
        [
            KeyboardButton(text="hh.uz"),
            KeyboardButton(text="ishonchsavdo.uz")
        ],
        [
            KeyboardButton(text="баннер(реклама на улице)"),
            KeyboardButton(text="флаер")
        ],
        [
            KeyboardButton(text="Знакомый / родственник / друг порекомендовал"),
            KeyboardButton(text="Отменить 🚫")
        ],
    ],
    resize_keyboard=True
)

ishorin_eng = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Telegram job search channel"),
            KeyboardButton(text="Olx.uz")
        ],
        [
            KeyboardButton(text="hh.uz"),
            KeyboardButton(text="ishonchsavdo.uz")
        ],
        [
            KeyboardButton(text="Billboard (outdoor advertising)"),
            KeyboardButton(text="Flyer")
        ],
        [
            KeyboardButton(text="Recommended by acquaintance / relative / friend"),
            KeyboardButton(text="Cancel 🚫")
        ],
    ],
    resize_keyboard=True
)
