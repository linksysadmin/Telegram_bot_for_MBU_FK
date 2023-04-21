import logging

from telebot.handler_backends import State, StatesGroup

logger = logging.getLogger(__name__)


class MyStates(StatesGroup):
    name = State()
    date_of_birthday = State()
    sex = State()
    email = State()
    phone_number = State()
    send_users_data = State()

    receive_resume = State()
    resume = State()

    university = State()
    season = State()

    test = State()
    question = State()

