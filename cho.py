import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'''Привет <b>{message.from_user.first_name}</b>! 👋 Я телеграмм-бот <b><i>«Что по корпусам»</i></b>, который поможет тебе найти дорогу до любого корпуса! 

Пропиши /next, чтобы продолжить пользоваться ботом. 😉'''
    photo = open('IMG_9017.JPEG', 'rb')
    bot.send_photo(message.chat.id, photo, caption=mess, parse_mode='HTML')


@bot.message_handler(commands=['next'])
def next(message):
    markup = InlineKeyboardMarkup()
    item1 = InlineKeyboardButton("корпус «А»", callback_data='А')
    item2 = InlineKeyboardButton("корпус «Б»", callback_data='Б')
    item3 = InlineKeyboardButton("корпус «В»", callback_data='В')
    item4 = InlineKeyboardButton("корпус «Г»", callback_data='Г')
    item5 = InlineKeyboardButton("корпус «Д»", callback_data='Д')
    item6 = InlineKeyboardButton("корпус «Л»", callback_data='Л')
    item7 = InlineKeyboardButton("корпус «К»", callback_data='К')
    item8 = InlineKeyboardButton("Спорткомплекс", callback_data='Спорт')
    item9 = InlineKeyboardButton("Варшава", callback_data='Варшава')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    bot.send_message(message.chat.id, "Где ты сейчас?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    if call.data == 'А':
        markup = InlineKeyboardMarkup()
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='АБ')
        item3 = InlineKeyboardButton("корпус «В»", callback_data='АВ')
        item4 = InlineKeyboardButton("корпус «Г»", callback_data='АГ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='АД')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='АЛ')
        item7 = InlineKeyboardButton("корпус «К»", callback_data='АК')
        item8 = InlineKeyboardButton("Спорткомплекс", callback_data='АСпорт')
        item9 = InlineKeyboardButton("Варшава", callback_data='АВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус А.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Б':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='БА')
        item3 = InlineKeyboardButton("корпус «В»", callback_data='БВ')
        item4 = InlineKeyboardButton("корпус «Г»", callback_data='БГ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='БД')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='БЛ')
        item7 = InlineKeyboardButton("корпус «К»", callback_data='БК')
        item8 = InlineKeyboardButton("Спорткомплекс", callback_data='БСпорт')
        item9 = InlineKeyboardButton("Варшава", callback_data='БВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус Б.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'В':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='ВА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='ВБ')
        item4 = InlineKeyboardButton("корпус «Г»", callback_data='ВГ')

        item6 = InlineKeyboardButton("корпус «Л»", callback_data='ВЛ')



        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)
        markup.add(item4)
        markup.add(item6)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус В.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Г':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='ГА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='ГБ')
        item3 = InlineKeyboardButton("корпус «В»", callback_data='ГВ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='ГД')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='ГЛ')
        item7 = InlineKeyboardButton("корпус «К»", callback_data='ГК')
        item8 = InlineKeyboardButton("Спорткомплекс", callback_data='ГСпорт')
        item9 = InlineKeyboardButton("Варшава", callback_data='ГВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус Г.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Д':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='ДА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='ДБ')

        item4 = InlineKeyboardButton("корпус «Г»", callback_data='ДГ')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='ДЛ')
        item7 = InlineKeyboardButton("корпус «К»", callback_data='ДК')
        item8 = InlineKeyboardButton("Спорткомплекс", callback_data='ДСпорт')
        item9 = InlineKeyboardButton("Варшава", callback_data='ДВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)

        markup.add(item4)
        markup.add(item6)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус Д.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Л':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='ЛА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='ЛБ')
        item3 = InlineKeyboardButton("корпус «В»", callback_data='ЛВ')
        item4 = InlineKeyboardButton("корпус «Г»", callback_data='ЛГ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='ЛД')
        item7 = InlineKeyboardButton("корпус «К»", callback_data='ЛК')
        item8 = InlineKeyboardButton("Спорткомплекс", callback_data='ЛСпорт')
        item9 = InlineKeyboardButton("Варшава", callback_data='ЛВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item7)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус Л.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'К':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='КА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='КБ')
        item3 = InlineKeyboardButton("корпус «В»", callback_data='КВ')
        item4 = InlineKeyboardButton("корпус «Г»", callback_data='КГ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='КД')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='КЛ')
        item8 = InlineKeyboardButton("Спорткомплекс", callback_data='КСпорт')
        item9 = InlineKeyboardButton("Варшава", callback_data='КВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали корпус K.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Спорт':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='СпортА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='СпортБ')

        item4 = InlineKeyboardButton("корпус «Г»", callback_data='СпортГ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='СпортД')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='СпортЛ')
        item8 = InlineKeyboardButton("корпус «К»", callback_data='СпортК')
        item9 = InlineKeyboardButton("Варшава", callback_data='СпортВаршава')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)

        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item8)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали Спорткомплекс.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Варшава':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("корпус «А»", callback_data='ВаршаваА')
        item2 = InlineKeyboardButton("корпус «Б»", callback_data='ВаршаваБ')
        item3 = InlineKeyboardButton("корпус «В»", callback_data='ВаршаваВ')
        item4 = InlineKeyboardButton("корпус «Г»", callback_data='ВаршаваГ')
        item5 = InlineKeyboardButton("корпус «Д»", callback_data='ВаршаваД')
        item6 = InlineKeyboardButton("корпус «Л»", callback_data='ВаршаваЛ')
        item7 = InlineKeyboardButton("корпус «К»", callback_data='ВаршаваК')
        item9 = InlineKeyboardButton("Спроткомплекс", callback_data='ВаршаваСпорт')

        item10 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')

        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        markup.add(item7)
        markup.add(item9)
        markup.add(item10)

        bot.send_message(call.message.chat.id, "Вы выбрали Варшава.\nВ какой корпус тебе нужно?",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'АБ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка АБ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка АБ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка АБ':
        video = open('Наземка АБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из А в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка АБ':
        video = open('Подземка АБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из А в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АВ':
        video = open('АВ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из А в В.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АГ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка АГ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка АГ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка АГ':
        video = open('Наземка АГ.MP4', 'rb')
        bot.send_video(call.message.chat.id, video, caption='Наземка из А в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка АГ':
        video = open('Подземка АГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из А в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АД':
        video = open('АД.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из А в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АЛ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка АЛ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка АЛ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка АЛ':
        video = open('Наземка АЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из А в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка АЛ':
        video = open('Подземка АЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из А в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АК':
        video = open('АК.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из А в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АСпорт':
        video = open('АСпорт.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из А в Спорткомплекс.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'АВаршава':
        video = open('АВаршава.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из А в Варшаву.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'БА':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка БА')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка БА')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка БА':
        video = open('Наземка БА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Б в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка БА':
        video = open('Подземка БА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Б в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БВ':
        video = open('БВ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Б в В.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БГ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка БГ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка БГ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)

        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка БГ':
        video = open('БГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Б в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка БГ':
        video = open('Подземка БГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Б в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БД':
        video = open('БД.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Б в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БЛ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка БЛ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка БЛ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка БЛ':
        video = open('Наземка БЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Б в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка БЛ':
        video = open('Подземка БЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Б в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БК':
        video = open('БК.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Б в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БСпорт':
        video = open('БСпорт.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Б в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'БВаршава':
        video = open('БВаршава.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Б в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'ВА':
        video = open('ВА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из В в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВБ':
        video = open('ВБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из В в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВГ':
        video = open('ВГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из В в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВЛ':
        video = open('ВЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из В в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'ГА':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка ГА')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка ГА')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ",parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка ГА':
        video = open('Наземка ГА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Г в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка ГА':
        video = open('Подземка ГА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Г в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГБ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка ГБ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка ГБ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка ГБ':
        video = open('Наземка ГБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Г в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка ГБ':
        video = open('Подземка ГБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Г в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГВ':
        video = open('ГВ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Г в В.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГД':
        video = open('ГД.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Г в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГК':
        video = open('ГК.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Г в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГЛ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка ГЛ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка ГЛ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка ГЛ':
        video = open('Наземка ГЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Г в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка ГЛ':
        video = open('Подземка ГЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Г в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГСпорт':
        video = open('ГСпорт.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Г в Спорткомплекс.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ГВаршава':
        video = open('ГВаршава.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Г в Варшаву.')
        bot.delete_message(call.message.chat.id, call.message.message_id)


    if call.data == 'ДА':
        video = open('ДА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДБ':
        video = open('ДБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДГ':
        video = open('ДГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДК':
        video = open('ДК.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДЛ':
        video = open('ДЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДСпорт':
        video = open('ДСпорт.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в Спорткомплекс.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ДВаршава':
        video = open('ДВаршава.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Д в Вараву.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'ЛА':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка ЛА')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка ЛА')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка ЛА':
        video = open('Наземка ЛА.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Л в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка ЛА':
        video = open('Подземка ЛА.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Л в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛБ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка ЛБ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка ЛБ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка ЛБ':
        video = open('Наземка ЛБ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Л в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка ЛБ':
        video = open('Подземка ЛБ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Л в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛВ':
        video = open('ЛВ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Л в В.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛГ':
        markup = InlineKeyboardMarkup()
        item1 = InlineKeyboardButton("Наземка", callback_data='наземка ЛГ')
        item2 = InlineKeyboardButton("Подземка", callback_data='Подземка ЛГ')
        item3 = InlineKeyboardButton("Возврат в главное меню", callback_data='back_to_menu')
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(call.message.chat.id, "Выберите способ прохода: ", parse_mode='html', reply_markup=markup)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'наземка ЛГ':
        video = open('Наземка ЛГ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Наземка из Л в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'Подземка ЛГ':
        video = open('Подземка ЛГ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Подземка из Л в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛД':
        video = open('ЛД.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Л в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛК':
        video = open('ЛК.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Л в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛСпорт':
        video = open('ЛСпорт.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Л в Спорткомплекс.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ЛВаршава':
        video = open('ЛВаршава.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Л в Варшаву.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'КА':
        video = open('КА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'КБ':
        video = open('КБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'КГ':
        video = open('КГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'КД':
        video = open('КД.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'КЛ':
        video = open('КЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'КСпорт':
        video = open('КСпорт.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в Спорткомплекс.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'КВаршава':
        video = open('КВаршава.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из К в Варшаву.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'СпортА':
        video = open('СпортА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СпортБ':
        video = open('СпортБ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'СпортГ':
        video = open('СпортГ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СпортД':
        video = open('СпортД.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СпортЛ':
        video = open('СпортЛ.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СпортК':
        video = open('СпортК.mp4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'СпортВаршава':
        video = open('СпортВаршава.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Спорткомплекса в Варшаву.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'ВаршаваА':
        video = open('ВаршаваА.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в А.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВаршаваБ':
        video = open('ВаршаваБ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в Б.')
        bot.delete_message(call.message.chat.id, call.message.message_id)



    if call.data == 'ВаршаваГ':
        video = open('ВаршаваГ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в Г.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВаршаваД':
        video = open('ВаршаваД.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в Д.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВаршаваЛ':
        video = open('ВаршаваЛ.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в Л.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВаршаваК':
        video = open('ВаршаваК.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в К.')
        bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == 'ВаршаваСпорт':
        video = open('ВаршаваСпорт.MP4', 'rb')
        bot.send_message(call.message.chat.id, 'Пожалуйста, подождите...')
        bot.send_video(call.message.chat.id, video, caption='Из Варшавы в Спорткомплекс.')
        bot.delete_message(call.message.chat.id, call.message.message_id)








    elif call.data == 'back_to_menu':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        next(call.message)


if __name__ == '__main__':
    bot.polling(none_stop=True)