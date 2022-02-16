"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import json
import logging
from datetime import date
from typing import Tuple

import ephem
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename='bot.log',
)


def greet_user(update, context) -> None:
    """Sets the rules for the command '/start'."""
    text = 'Вызван /start'
    update.message.reply_text(text)


def get_constellation(update, context) -> None:
    """Sets the rules for the command '/planets'."""
    text = '''Для того чтобы узнать в каком созвездии\
     находится планета введите сообщение "/planet Mars"'''
    update.message.reply_text(text)


def talk_to_me(update, context):
    """The function to make answer message."""
    user_text = update.message.text
    text_list = user_text.split(' ')
    planet_date = date.today()
    if text_list[0] == '/planet':
        constellation = translater(planet_name(text_list[1], planet_date))
        user_text = 'Планета {0} в созвездии {1} ({2})'.format(
            text_list[1],
            constellation[0],
            constellation[1],
        )
    update.message.reply_text(user_text)


def planet_name(planet: str, current_date: date) -> str:
    """The function determines in which constellation the planet is located.

    Args:
        planet (str): the planet for which the constellation is determined
        current_date (date): time to determine constellation

    Returns:
        str: constellation name
    """
    planet_scheme = {
        'Mercury': ephem.Mercury,
        'Venus': ephem.Venus,
        'Mars': ephem.Mars,
        'Jupiter': ephem.Jupiter,
        'Saturn': ephem.Saturn,
        'Pluto': ephem.Pluto,
        'Neptune': ephem.Neptune,
        'Uranus': ephem.Uranus,
    }
    if planet_scheme.get(planet):
        return ephem.constellation(
            planet_scheme[planet](current_date),
        )[1]
    return 'No such planet'


def translater(word: str, lang_pair: str = 'en|ru') -> Tuple[str, str]:
    """Translate function.

    This function translate constellation name to Russian.

    Args:
        word (str): word for translation.
        lang_pair (str): you can choose rule ti translate like:\
            en|ru - from english to russian.

    Returns:
        str: Russian word
    """
    base_url = 'https://api.mymemory.translated.net/'
    url = f'{base_url}get?q={word}&langpair={lang_pair}'
    try:
        rus_word = requests.request(
            'GET', url,
        ).json()['responseData']['translatedText']
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.SSLError,
        json.decoder.JSONDecodeError,
    ):
        rus_word = ''
    return (word, rus_word)


def main():
    """Start bot function."""
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planets', get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
