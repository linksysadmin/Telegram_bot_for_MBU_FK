import logging

from handlers.keyboards import remove_keyboard

logger = logging.getLogger(__name__)


def send_users_data(message, bot):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        print(f'отправка в бд НУЖНО СДЕЛАТЬ!!!!!!!!!! {data}')
    remove_keyboard(message, bot, 'Ваши данные отправлены!')
    bot.delete_state(message.from_user.id, message.chat.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


