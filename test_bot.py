import time
import telebot
from telebot import apihelper
from money import money_status
from weatherapi import weather
from find_news import get_news
import cats
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


"""------------------------------------------functions---------------------------------------------------------------"""


@bot.message_handler(func=lambda message: True, content_types=['location'])
def user_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    bot.send_message(message.chat.id, weather(lat, lon))
"""

@bot.message_handler(content_types=['text'])
def send_msg(message):
    if message.text == '🐱':
        bot.send_message(message.chat.id, text=cat(), reply_to_message_id=message.message_id)

"""
@bot.message_handler(commands=['buttons'])
def buttons_start(message):
    first_markup = telebot.types.ReplyKeyboardMarkup(True)
    but_start = telebot.types.KeyboardButton('/start')
    but_help = telebot.types.KeyboardButton('/help')
    but_info = telebot.types.KeyboardButton('/info')
    but_com = telebot.types.KeyboardButton('/more')
    first_markup.add(but_start, but_help, but_info, but_com,)
    bot.send_message(message.chat.id, "Лови кнопки приятель⚙️", reply_markup=first_markup)


@bot.message_handler(commands=['more'])
def buttons_more(message):
    func_markup = telebot.types.ReplyKeyboardMarkup(True)
    but_wth = telebot.types.KeyboardButton('/weather☁', request_location=True)
    but_nws = telebot.types.KeyboardButton('/news📰')
    but_mny = telebot.types.KeyboardButton('/money💰')
    but_first = telebot.types.KeyboardButton('/buttons')
    func_markup.add(but_wth, but_nws, but_mny, but_first,)
    bot.send_message(message.chat.id, "Лови ещё кнопки приятель⚙️", reply_markup=func_markup)


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
    but_lenta = telebot.types.InlineKeyboardButton(text='Лента.ру', callback_data='https://m.lenta.ru')
    but_med = telebot.types.InlineKeyboardButton(text='Медуза', callback_data='https://meduza.io')
    but_ria = telebot.types.InlineKeyboardButton(text='РИА новости', callback_data='https://ria.ru')
    key.row(but_lenta, but_med, but_ria)
    bot.send_message(message.chat.id, "НОВОСТИ", reply_markup=key)


@bot.message_handler(commands=['cats'])
def cat_pic(message):
    key_cat = telebot.types.InlineKeyboardMarkup(True)
    but_pic = telebot.types.InlineKeyboardButton(text='КАРТИНКА', callback_data='pic')
    but_gif = telebot.types.InlineKeyboardButton(text='ГИФКА', callback_data='gif')
    key_cat.row(but_pic, but_gif)
    bot.send_photo(message.chat.id, 'https://pp.userapi.com/c846524/v846524528/1c75bc/_xJsz6A9Wec.jpg',
                   reply_markup=key_cat)


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    news_key = telebot.types.InlineKeyboardMarkup(True)
    but_link = telebot.types.InlineKeyboardButton(text='Перейти на сайт', url=call.data)
    news_key.add(but_link)

    key_cat = telebot.types.InlineKeyboardMarkup(True)
    but_pic = telebot.types.InlineKeyboardButton(text='КАРТИНКА', callback_data='pic')
    but_gif = telebot.types.InlineKeyboardButton(text='ГИФКА', callback_data='gif')
    key_cat.row(but_pic, but_gif)

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
    elif call.data == 'pic':
        bot.send_photo(call.message.chat.id, cats.get_cats('pic'), reply_markup=key_cat)
    elif call.data == 'gif':
        bot.send_document(call.message.chat.id, cats.get_cats('gif'), reply_markup=key_cat)


while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
