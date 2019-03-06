import time
import telebot
from telebot import apihelper
from money import money_status
from weatherapi import weather
from find_news import get_news
#apihelper.proxy = {'https': 'socks5://352354383:RiqvhK6t@phobos.public.opennetwork.cc:1090'}
apihelper.proxy = {'https': 'socks5://352354383:RiqvhK6t@deimos.public.opennetwork.cc:1090'}
TOKEN = "559015083:AAFmBW3TV6NEX579WlMEmgDczsuLekDxPIg"
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])  # welcome message handler
def send_msg(message):
    bot.send_message(message.chat.id, 'Привет, это демонстративный бот,в нем ты найдешь реализацию различных функций,\n'
                                      'для того,что бы посмотреть что я умею напиши /help')


@bot.message_handler(commands=['help'])  # help message handler
def send_welcome(message):
    bot.send_message(message.chat.id, '/start\n/help\n/info\n/buttons')


@bot.message_handler(commands=['info'])
def send_msg(message):
    bot.send_message(message.chat.id, '😉\ncreated by: @Sweet_Sempai\n github: https://github.com/sweetsenpai')


@bot.message_handler(func=lambda message: True, content_types=['location'])
def user_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    bot.send_message(message.chat.id, weather(lat, lon))


@bot.message_handler(commands=['buttons'])
def buttons_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    but_1 = telebot.types.KeyboardButton('/weather☁', request_location=True)
    but_2 = telebot.types.KeyboardButton('/start')
    but_3 = telebot.types.KeyboardButton('/help')
    but_4 = telebot.types.KeyboardButton('/info')
    but_5 = telebot.types.KeyboardButton('/news📰')
    but_6 = telebot.types.KeyboardButton('/money💰')
#    user_markup.row('/start', '/help', '/info')
#   user_markup.row(but_1, '/news📰', '/money💰')
    user_markup.add(but_1, but_2, but_3,
                    but_4, but_5, but_6)
    bot.send_message(message.chat.id, "Лови кнопки приятель⚙️", reply_markup=user_markup)
   

@bot.message_handler(commands=['money💰'])
def money(message):
    money_key = telebot.types.InlineKeyboardMarkup(True)
    EUR = telebot.types.InlineKeyboardButton(text='€💶', callback_data='EUR')
    DOL = telebot.types.InlineKeyboardButton(text='$💵', callback_data='USD')
    ALL = telebot.types.InlineKeyboardButton(text='Все доступные валюты', callback_data='ALL')
    money_key.add(EUR, DOL, ALL)
    bot.send_message(message.chat.id, "КУРСЫ ВАЛЮТ", reply_markup=money_key)


@bot.message_handler(commands=['news📰'])
def inline(message):
    key = telebot.types.InlineKeyboardMarkup(True)
    but_1 = telebot.types.InlineKeyboardButton(text='Лента.ру', callback_data='https://m.lenta.ru')
    but_2 = telebot.types.InlineKeyboardButton(text='Медуза', callback_data='https://meduza.io')
    but_3 = telebot.types.InlineKeyboardButton(text='РИА новости', callback_data='https://ria.ru')
    key.row(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "НОВОСТИ", reply_markup=key)


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    news_key = telebot.types.InlineKeyboardMarkup(True)
    but_link = telebot.types.InlineKeyboardButton(text='Перейти на сайт', url=call.data)

    news_key.add(but_link)
    if call.data == 'EUR':
        bot.send_message(call.message.chat.id, money_status('EUR'))
    elif call.data == 'USD':
        bot.send_message(call.message.chat.id, money_status('USD'))
    elif call.data == 'ALL':
        bot.send_message(call.message.chat.id, money_status('ALL'))
    elif call.data == 'https://m.lenta.ru':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.data, reply_markup=news_key)
        bot.send_message(call.message.chat.id, text='Главная новость на данный момент:')
        bot.send_message(call.message.chat.id, get_news(call.data))
    elif call.data == 'https://meduza.io':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.data, reply_markup=news_key)
        bot.send_message(call.message.chat.id, text='Главная новость на данный момент:')
        bot.send_message(call.message.chat.id, get_news(call.data))
    elif call.data == 'https://ria.ru':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=call.data, reply_markup=news_key)
        bot.send_message(call.message.chat.id, text='Главная новость на данный момент:')
        bot.send_message(call.message.chat.id, get_news(call.data))



while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
