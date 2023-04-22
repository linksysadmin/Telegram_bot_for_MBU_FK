import logging
import re
from datetime import datetime

import telebot

from config import REDIS

logger = logging.getLogger(__name__)


class CheckDirection(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_direction'

    def check(self, message):
        if message.text in ('Стажировка', 'Практика'):
            return True
        else:
            return False


class CheckUserName(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_name'

    def check(self, message):
        name = message.text
        if len(name.split()) == 3:
            return True
        else:
            return False


class CheckDate(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_date'

    def check(self, message):
        try:
            datetime.strptime(message.text, '%Y-%m-%d')
            return True
        except ValueError:
            return False


class CheckSex(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_sex'

    def check(self, message):
        if message.text in ['Мужской', 'Женский']:
            return True
        else:
            return False


class CheckEmail(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_email'

    def check(self, message):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$')
        if bool(pattern.match(str(message.text))) is True:
            return True
        else:
            return False


class CheckPhoneNumber(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_phone'

    def check(self, message):
        pattern = re.compile(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
        if bool(pattern.match(str(message.text))) is True:
            return True
        else:
            return False


class ContactForm(telebot.custom_filters.SimpleCustomFilter):
    key = 'contact_form'

    def check(self, message):
        return message.contact is not None


class CheckConsent(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_consent'

    def check(self, message):
        if message.text == 'Отправить':
            return True
        else:
            return False


class CheckAnswer(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_answer'

    def check(self, message):
        if message.text == 'Да':
            return True
        else:
            return False


class CheckFile(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_file'

    def check(self, message):
        if message.document is not None:
            return True
        else:
            return False


class CheckUniversity(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_university'

    def check(self, message):
        if message.text in ('1.РАНХиГС', '2.Финунивер', '3.РГГУ', '4.РУТ МИИТ', '5.ГУУ', '6.МИРЭА',
                            '7.МИСИС', '8.РУДН', '9.РЭУ им. Плеханова', '10.ВАВТ', '11.МЭИ'):
            return True
        else:
            return False


class CheckSeason(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_season'

    def check(self, message):
        if message.text in ('Весна', 'Лето', 'Зима', 'Осень'):
            return True
        else:
            return False


class CheckAnswerInTest(telebot.custom_filters.SimpleCustomFilter):
    key = 'check_answer_in_test'

    def check(self, message):
        if message.text in (
                '4', '9', '2', 'Зеленый', 'Желтый', 'Синий', 'Бразилия', 'Канада', 'Мексика', 'Варшава', 'Париж',
                'Иерусалим', 'Умный', 'Смешной', 'Спящий', 'Серебро', 'Медь', 'Золото', 'Медсестра',
                'Костоправ', 'Хирург', 'Квадрат', 'Круг', 'Треугольник', 'Кенгуру', 'Коала', 'Лев', 'Ислам',
                'Иудаизм', 'Буддизм'):
            return True
        else:
            return False


def check_user_in_direction(user_id: int) -> bool:
    direction = REDIS.get(f'user:{user_id}:check_direction')
    logger.info(f'{direction}: {user_id}')
    if direction is not None:
        return True
    else:
        return False
