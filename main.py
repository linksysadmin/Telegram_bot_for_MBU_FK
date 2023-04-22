# -*- coding: utf-8 -*-

import logging

import flask
import telebot
from telebot import custom_filters
from telebot.storage import StateRedisStorage

from config import TELEGRAM_BOT_API_TOKEN, WEBHOOK_URL_PATH
from handlers import callback
from handlers.administrator_function import check_password_and_add_admin_to_db
from handlers.commands import start, info, test_, survey, resume, university, info_personal_reception, season, feedback, \
    get_excel_and_send_to_user
from handlers.get_info_from_user import get_user_name, get_date_of_birthday, name_incorrect, date_incorrect, \
    get_user_sex, sex_incorrect, get_user_email, email_incorrect, get_user_phone, phone_incorrect, delete_state_, \
    get_university, university_incorrect, receive_resume, resume_incorrect, choose_direction, direction_incorrect, \
    get_season, season_incorrect
from handlers.send_data import send_users_data
from handlers.test_for_users import get_answer_to_question, start_test
from services.states import MyStates
from services.filters import CheckDate, CheckPhoneNumber, CheckUserName, CheckSex, CheckConsent, CheckEmail, \
    CheckAnswerInTest, ContactForm, CheckAnswer, CheckFile, CheckUniversity, CheckDirection, CheckSeason

logging.basicConfig(handlers=(logging.StreamHandler(),),
                    format="%(name)s %(asctime)s - %(levelname)s - %(message)s",
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TELEGRAM_BOT_API_TOKEN, state_storage=StateRedisStorage(), parse_mode='HTML')

FILTERS = (custom_filters.StateFilter(bot),
           custom_filters.IsDigitFilter(),
           custom_filters.TextMatchFilter(),
           CheckDirection(),
           CheckUserName(),
           CheckDate(),
           CheckSex(),
           CheckEmail(),
           CheckPhoneNumber(),
           ContactForm(),
           CheckConsent(),
           CheckAnswer(),
           CheckFile(),
           CheckUniversity(),
           CheckSeason(),
           CheckAnswerInTest()
           )

# Function for commands
COMMAND_HANDLERS = {
    "start": start,
    "info": info,
    "test": test_,
    "survey": survey,
    "resume": resume,
    "university": university,
    "season": season,
    "info_personal_reception": info_personal_reception,
    "feedback": feedback,
    "get_excel": get_excel_and_send_to_user,
}


def register_functions_for_bot():
    """Регистрация команд, фильтров, состояний и функций обратного вызова для Телеграм-бота"""

    """   Регистрация команд telegram бота """

    for command_name, command_handler in COMMAND_HANDLERS.items():
        bot.register_message_handler(commands=[command_name], callback=command_handler, pass_bot=True)
    bot.register_message_handler(state="*", callback=delete_state_, commands=['cancel'], pass_bot=True)

    """   Добавление фильтров сообщений   """

    for filter_ in FILTERS:
        bot.add_custom_filter(filter_)

    """   Регистрация состояний пользователя   """

    bot.register_message_handler(state="*", text=['Отменить'], callback=delete_state_, pass_bot=True)

    bot.register_message_handler(state=MyStates.choose_direction, callback=choose_direction, pass_bot=True,
                                 check_direction=True)
    bot.register_message_handler(state=MyStates.choose_direction, callback=direction_incorrect, pass_bot=True,
                                 check_direction=False)

    bot.register_message_handler(state=MyStates.name, callback=get_user_name, pass_bot=True, check_name=True)
    bot.register_message_handler(state=MyStates.name, callback=name_incorrect, pass_bot=True, check_name=False)

    bot.register_message_handler(state=MyStates.date_of_birthday, callback=get_date_of_birthday, pass_bot=True,
                                 check_date=True)
    bot.register_message_handler(state=MyStates.date_of_birthday, callback=date_incorrect, pass_bot=True,
                                 check_date=False)

    bot.register_message_handler(state=MyStates.sex, callback=get_user_sex, pass_bot=True, check_sex=True)
    bot.register_message_handler(state=MyStates.sex, callback=sex_incorrect, pass_bot=True, check_sex=False)

    bot.register_message_handler(state=MyStates.email, callback=get_user_email, pass_bot=True, check_email=True)
    bot.register_message_handler(state=MyStates.email, callback=email_incorrect, pass_bot=True, check_email=False)

    bot.register_message_handler(state=MyStates.phone_number, callback=get_user_phone, pass_bot=True, contact_form=True,
                                 check_phone=False)
    bot.register_message_handler(state=MyStates.phone_number, callback=get_user_phone, pass_bot=True, check_phone=True)
    bot.register_message_handler(state=MyStates.phone_number, callback=phone_incorrect, pass_bot=True,
                                 check_phone=False)

    bot.register_message_handler(state=MyStates.send_users_data, callback=send_users_data, pass_bot=True)

    bot.register_message_handler(state=MyStates.test, callback=start_test, pass_bot=True)
    bot.register_message_handler(state=MyStates.question, callback=get_answer_to_question, pass_bot=True,
                                 check_answer_in_test=True)

    bot.register_message_handler(state=MyStates.resume, callback=receive_resume, pass_bot=True, check_file=True)
    bot.register_message_handler(state=MyStates.resume, callback=resume_incorrect, pass_bot=True, check_file=False)

    bot.register_message_handler(state=MyStates.university, callback=get_university, pass_bot=True,
                                 check_university=True)
    bot.register_message_handler(state=MyStates.university, callback=university_incorrect, pass_bot=True,
                                 check_university=False)

    bot.register_message_handler(state=MyStates.season, callback=get_season, pass_bot=True, check_season=True)
    bot.register_message_handler(state=MyStates.season, callback=season_incorrect, pass_bot=True, check_season=False)

    bot.register_message_handler(state=MyStates.password, callback=check_password_and_add_admin_to_db, pass_bot=True)

    """   Регистрация обработчиков нажатий на клавиатуру   """

    bot.register_callback_query_handler(func=lambda callback: callback.data == "info",
                                        callback=callback.callback_info, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "test",
                                        callback=callback.callback_test, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "survey",
                                        callback=callback.callback_survey, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "resume",
                                        callback=callback.callback_resume, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "university",
                                        callback=callback.callback_university, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "season",
                                        callback=callback.callback_season, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "info_personal_reception",
                                        callback=callback.callback_info_personal_reception, pass_bot=True)
    bot.register_callback_query_handler(func=lambda callback: callback.data == "feedback",
                                        callback=callback.callback_feedback, pass_bot=True)


register_functions_for_bot()
bot.infinity_polling(skip_pending=True)
# app = flask.Flask(__name__)


# @app.route('/', methods=['GET', 'HEAD'])
# def index():
#     return 'OK'
#
#
# # Обработка POST-запроса от Telegram Bot API
# @app.route(WEBHOOK_URL_PATH, methods=['POST'])
# def webhook():
#     """Обработка http-запросов, которые telegram пересылает на наш сервер"""
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)
