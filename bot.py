#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s\n%(message)s',
                    level=logging.INFO)

logger = logging.getLogger("")

messages = ['Они все уже в Нижнем Тагиле, отрабатывают...',
            'Северные олени?! Когда же Вы свой ягель найдёте??!!',
            'Трохрогая, это максимум на что Вы способны?',
            'Уважаемый абитуриент! Тебе все предыдущие товарищи почти правильно написали! Ты просто пошарь по ихним профайлам и все узнаешь!!! Особенно обрати внимание на их очень средний балл!',
            'Я никогда серьёзно не считал, что web-программист может представлять какие-то знания !',
            'А про надо понадобившеяся знания спросите у НИИСА-АГАТ',
            'Смешно!!!',
            'Конь, а можно мимо нас?!',
            'Я тебе просто не завидую, ну ты полнейший МУДАК!!!',
            'Да, тогда объясните, пожалуйста, как площадь круга может быть в 2,5 раза больше площади прямоугольника?! Это я видел, но я в это не верю!!!',
            'Ваня! И Вы во все это верите?! Попробуем дальше через Вас запускать нужные вещи! Спасибо за содействие!!!',
            'Спасибо за диагноз! До встречи, когда мне придётся ВАШ бред диагностировать!',
            'Ваня! Спасибо за готовность говорить, но мы очень круто работаем!!',
            'Это Вы о знаниях мощной специализации ПИ?',
            'Вы все ещё на четвёртом?!',
            'а как-то нам на... все на... рать!',
            'Ребята, извините! А чего Вы сюда приперлись! Выбор-то раньше надо делать!!!',
            'А колхоз возглавить не пробовал???',
            'Как же Вы ограничены своей ТРОХРОГАСЦЮ?!',
            'Cудя по Вашему быстрому ответу с ограничением у Вас все в порядке!',
            'Это ж надо на ФПМИ в 21 веке: прежде чем добраться до нормального человека, надо прочитать Шизы шести человек..',
            'Мне вас жаль, вопрос-то был актуальный, а вот ответы тупизной попахивают..',
            'Cпасибо, первый честный на ФПМИ',
            'Мне жаль поэтому нормальных людей, которые хотят нормальные ответы услышать, а тут Вы со своей ненормальной ориентацией, а мы после этого должны усе вставать??!!',
            'Мне просто жаль Вас, пытающегося быть ПЕтросяном или Мартиросяном??? Попробуйте быть просто Мандриком?!',
            'Пошло понимание!!',
            'Может перевести Вам, то что Вы так и не поняли??',
            'Дадастали!!!']

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Пока я дед нихто! Только не забудь это скопировать! А потом поговорим, может быть!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def echo(bot, update):
    time.sleep(2)
    message = messages[randint(0, len(messages) - 1)]
    bot.sendMessage(update.message.chat_id, text = message)
    logger.info(update.message.from_user.first_name + ' ' + update.message.from_user.last_name + ': ' + update.message.text
     + '\nSechko: '+ message.decode('utf-8'))

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater('token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler([Filters.text], echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
