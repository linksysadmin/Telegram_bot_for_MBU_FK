import logging

from handlers.keyboards import keyboard_yes_or_no, remove_keyboard, keyboard_university
from services.states import MyStates

logger = logging.getLogger(__name__)


def send_users_data(message, bot):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        print(f'отправка в бд {data}')
    bot.send_message(message.chat.id, f'Ваши данные отправлены, готовы ли вы предоставить резюме?',
                     reply_markup=keyboard_yes_or_no())
    bot.set_state(message.chat.id, MyStates.resume, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def resume_answer_yes(message, bot):
    remove_keyboard(message, bot, f'Отправьте файл')
    bot.set_state(message.chat.id, MyStates.receive_resume, message.from_user.id)


def resume_answer_no(message, bot):
    bot.send_message(message.chat.id, f'Выберите ВУЗ',
                     reply_markup=keyboard_university())
    bot.set_state(message.chat.id, MyStates.university, message.from_user.id)


def receive_resume(message, bot):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Сохраняем файл на сервере
    src = message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.delete_state(message.from_user.id, message.chat.id)
    logger.info(f'State пользователя удалён -- {bot.get_state(message.from_user.id, message.chat.id)}')


def resume_incorrect(message, bot):
    bot.send_message(message.chat.id, f'Это не файл')
