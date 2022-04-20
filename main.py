import requests
import json
import telebot
from datetime import datetime
import time
from buttons import *
from telebot import types
vremya = (datetime.now().strftime('%H:%M'))
sana  = datetime.now().strftime("%d.%m.%Y")
token = '5276721532:AAHmE-kHCuKh-GrKb2WWdn_yYXdjSfL5ZV4'
r = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/')
data = r.json()
info = f"""
	Valyutalar Kursi

	Sana:{sana}\n\n
	🇺🇸 1 USD:🇺🇿{data[0]['Rate']} sum 📊{data[0]['Diff']}\n
	🇪🇺 1 EURO:🇺🇿{data[1]['Rate']} sum 📊{data[1]['Diff']}\n
	🇷🇺 1 Rubl:🇺🇿{data[2]['Rate']} sum 📊{data[2]['Diff']}
	"""
info_ru = f"""
	Курс валюты

	Дата:{sana}\n\n
	🇺🇸 1 USD:🇺🇿{data[0]['Rate']} sum 📊{data[0]['Diff']}\n
	🇪🇺 1 EURO:🇺🇿{data[1]['Rate']} sum 📊{data[1]['Diff']}\n
	🇷🇺 1 Rubl:🇺🇿{data[2]['Rate']} sum 📊{data[2]['Diff']}
	"""
bot = telebot.TeleBot(token,parse_mode='HTML')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id,f"""
		Assalomu aleykum {message.from_user.first_name} botga Xush kelibsiz!
		Marxamat Tilni tanlab Bot Funksiyalaridan Foydalishingiz mumkin\n
		Привет {message.from_user.first_name} Добро пожаловать в бота!
		Выбрайте язык и использовайте функции бота
		""",reply_markup=markup_ln)
@bot.message_handler(content_types='text')
def getData(message):
	a = []
    
    
	if message.text == "🇷🇺Russian":
		bot.send_message(message.chat.id,info_ru,reply_markup=markup_ru)
		dic = {
			'lg':'ru',
			'id':message.chat.id
		}
		a.append(dic)
	elif message.text == '🇺🇿Uzbek':
		bot.send_message(message.chat.id,info,reply_markup=markup_uz)
		dic = {
					'lg':'uz',
					'id':message.chat.id
				}
		a.append(dic)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.data == "resetData_ru":	
		bot.send_message(call.message.chat.id,info_ru,reply_markup=markup_ru)
		time.sleep(2)
	elif call.data == 'resetData_uz':
		bot.send_message(call.message.chat.id,info,reply_markup=markup_uz)
bot.infinity_polling()

