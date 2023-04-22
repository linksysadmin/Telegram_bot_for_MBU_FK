import json
import logging
from datetime import datetime

from config import REDIS, TELEGRAM_GROUP_CHAT_ID
from handlers.keyboards import keyboard_sex, keyboard_consent_to_send_data, remove_keyboard, keyboard_enter_menu, \
    keyboard_send_phone, keyboard_university
from services.send_info_to_database import update_data
from services.states import MyStates

logger = logging.getLogger(__name__)


def choose_direction(message, bot):
    bot.add_data(message.from_user.id, message.chat.id, direction=message.text)
    remove_keyboard(message, bot, 'Введите Ваши: Фамилию Имя Отчество через пробел')
    bot.set_state(message.chat.id, MyStates.name, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_user_name(message, bot):
    """ STATE 5 Получение имени от пользователя. """
    bot.add_data(message.from_user.id, message.chat.id, name=message.text)
    bot.send_message(message.chat.id, 'Укажите дату рождения в формате: ГГГГ-ММ-ДД\nПример: 2003-03-21')
    bot.set_state(message.chat.id, MyStates.date_of_birthday, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_date_of_birthday(message, bot):
    """ STATE 2 - Получение дня рождения пользователя. """
    date_of_birthday = datetime.strptime(message.text, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - date_of_birthday.year - (
            (today.month, today.day) < (date_of_birthday.month, date_of_birthday.day))
    data = {
        'date_of_birthday': date_of_birthday.strftime('%Y-%m-%d'),
        'age': age
    }
    bot.add_data(message.from_user.id, message.chat.id, **data)
    bot.send_message(message.chat.id, 'Укажите ваш пол:', reply_markup=keyboard_sex())
    bot.set_state(message.chat.id, MyStates.sex, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_user_sex(message, bot):
    """ STATE 2 - Получение дня рождения пользователя. """
    bot.add_data(message.from_user.id, message.chat.id, sex=message.text)
    remove_keyboard(message, bot, 'Укажите Ваш email:')
    bot.set_state(message.chat.id, MyStates.email, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_user_email(message, bot):
    """ STATE 2 - Получение дня рождения пользователя. """
    bot.add_data(message.from_user.id, message.chat.id, email=message.text)
    bot.send_message(message.chat.id, 'Укажите Ваш номер телефона:', reply_markup=keyboard_send_phone())
    bot.set_state(message.chat.id, MyStates.phone_number, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_user_phone(message, bot):
    """ STATE 3 - Получение номера телефона от пользователя."""
    phone = message.text
    if message.contact is not None:
        phone = message.contact.phone_number
    bot.add_data(message.from_user.id, message.chat.id, phone=phone)
    bot.send_message(message.chat.id, 'Отправить данные?', reply_markup=keyboard_consent_to_send_data())
    bot.set_state(message.chat.id, MyStates.send_users_data, message.from_user.id)


def receive_resume(message, bot):
    bot.send_document(chat_id=TELEGRAM_GROUP_CHAT_ID, document=message.document.file_id,
                      caption=f'Резюме от пользователя:\n{message.from_user.first_name}',
                      disable_content_type_detection=True)
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, f'Резюме получено!', )
    logger.info(f'State пользователя удалён -- {bot.get_state(message.from_user.id, message.chat.id)}')


def get_university(message, bot):
    direction = json.loads(REDIS.get(f'user:{message.from_user.id}:check_direction'))
    update_data(f'{direction}', 'university', message.text, message.from_user.id)
    remove_keyboard(message, bot, 'Университет выбран. Теперь пройдите тест: /test')
    bot.delete_state(message.from_user.id, message.chat.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_season(message, bot):
    direction = json.loads(REDIS.get(f'user:{message.from_user.id}:check_direction'))
    update_data(f'{direction}', 'season', message.text, message.from_user.id)
    remove_keyboard(message, bot, 'Период выбран. Теперь выберите ВУЗ нажав: /university')
    bot.delete_state(message.from_user.id, message.chat.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def direction_incorrect(message, bot):
    bot.send_message(message.chat.id, f'Направление не выбрано!')


def resume_incorrect(message, bot):
    bot.send_message(message.chat.id, f'Это не файл')


def name_incorrect(message, bot):
    """Некорректный ввод имени"""
    bot.send_message(message.chat.id, 'Введите в формате: Фамилия Имя Отчество\nПример: Головин Николай Петрович')


def date_incorrect(message, bot):
    """Некорректный ввод даты"""
    bot.send_message(message.chat.id, 'Дата указана неверно, укажите дату в формате: ГГГГ-ММ-ДД\nПример: 2003-03-21')


def sex_incorrect(message, bot):
    bot.send_message(message.chat.id, 'Вы указали неверный пол')


def email_incorrect(message, bot):
    bot.send_message(message.chat.id, 'Укажите email в формате: example@yandex.ru')


def phone_incorrect(message, bot):
    """Некорректный ввод телефона"""
    bot.send_message(message.chat.id, 'Некорректный ввод.\nВведите в формате:\n\n"+7XXXXXXXXXX",\n'
                                      '8XXXXXXXXXX\n9XXXXXXXXX\n\nПример: 89953423452')


def season_incorrect(message, bot):
    bot.send_message(message.chat.id, 'Время года не выбрано!')


def university_incorrect(message, bot):
    bot.send_message(message.chat.id, 'Вы не выбрали университет из предложенных')


def delete_state_(message, bot):
    """ Выход из STATE """
    remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, 'Главное меню',
                     reply_markup=keyboard_enter_menu())
    bot.delete_state(message.from_user.id, message.chat.id)
    logger.info(f'State пользователя удалён -- {bot.get_state(message.from_user.id, message.chat.id)}')
