import logging

from handlers.text_messages import TEXT_MESSAGES
from handlers.keyboards import remove_keyboard, keyboard_enter_menu, keyboard_yes_or_no, keyboard_for_test, \
    keyboard_university, keyboard_for_survey, keyboard_seasons
from services.states import MyStates

logger = logging.getLogger(__name__)


def start(message, bot):
    logger.info(f'User {message.from_user.first_name} started a conversation with the bot')
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['start'].format(username=f'{message.from_user.first_name}'), reply_markup=keyboard_enter_menu())
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def info(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')

    bot.send_message(message.chat.id, TEXT_MESSAGES['info'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def test_(message, bot) -> None:
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id,
                     TEXT_MESSAGES['test_'], reply_markup=keyboard_for_test())
    bot.set_state(message.chat.id, MyStates.test, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def survey(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['survey'], reply_markup=keyboard_for_survey())
    bot.set_state(message.chat.id, MyStates.choose_direction, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def resume(message, bot):
    bot.send_message(message.chat.id, TEXT_MESSAGES['resume'])
    bot.set_state(message.chat.id, MyStates.resume, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def university(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['university'], reply_markup=keyboard_university())
    bot.set_state(message.chat.id, MyStates.university, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def season(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['season'], reply_markup=keyboard_seasons())
    bot.set_state(message.chat.id, MyStates.season, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def info_personal_reception(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['info_personal_reception'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def feedback(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['feedback'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


commands_to_message = {
    "start": start,
    "info": info,
    "test": test_,
    "survey": survey,
    "resume": resume,
    "university": university,
    "season": season,
    "info_personal_reception": info_personal_reception,
    "feedback": feedback,
}
