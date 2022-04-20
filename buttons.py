
from pickle import TRUE
from telebot import types
button = ['🇺🇿Uzbek','🇷🇺Russian']




markup_ln = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard = True)
markup_ln.add(*[types.KeyboardButton(advert) for advert in button])

markup_ru = types.InlineKeyboardMarkup()
resetDataKey = types.InlineKeyboardButton("Обновить", callback_data="resetData_ru")
markup_ru.add(resetDataKey)


markup_uz = types.InlineKeyboardMarkup()
resetDataKey = types.InlineKeyboardButton("Yangilash", callback_data="resetData_uz")
markup_uz.add(resetDataKey)
