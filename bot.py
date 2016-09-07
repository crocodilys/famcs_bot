#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

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
            'Ваня! Спасибо за готовность говорить, но мы очень круто работаем!!']

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Пока я дед нихто! Только не забудь это скопировать! А потом поговорим, может быть!')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=messages[randint(0, len(messages) - 1)])

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater("TOKEN")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler([Filters.text], echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
