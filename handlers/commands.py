import logging

from handlers.text_messages import TEXT_MESSAGES
from handlers.keyboards import remove_keyboard, keyboard_enter_menu, keyboard_yes_or_no
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
                     TEXT_MESSAGES['about'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def survey(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['help_'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def resume(message, bot):
    bot.send_message(message.chat.id, TEXT_MESSAGES['resume'], reply_markup=keyboard_yes_or_no())
    bot.set_state(message.chat.id, MyStates.resume, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def university(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['help_'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def season(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['help_'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def info_personal_reception(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['help_'])
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def feedback(message, bot):
    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        bot.delete_state(message.from_user.id, message.chat.id)
        remove_keyboard(message, bot, 'Отменено')
    bot.send_message(message.chat.id, TEXT_MESSAGES['help_'])
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
