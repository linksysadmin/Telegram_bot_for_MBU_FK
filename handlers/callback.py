import logging

from handlers.keyboards import remove_keyboard, keyboard_enter_menu, keyboard_question1, keyboard_for_test
from services.states import MyStates
from handlers.text_messages import TEXT_MESSAGES

logger = logging.getLogger(__name__)


def callback_enter_menu(call, bot):
    logger.info(f'Отработка callback: {call.data}')
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                          text='Выберите то, что вам нужно: ⬇', reply_markup=keyboard_enter_menu())


def callback_info(call, bot):
    logger.info(f'Отработка callback: {call.data}')
    bot.send_message(chat_id=call.message.chat.id, message_id=call.message.id,
                     text=TEXT_MESSAGES['info'])


def callback_test(call, bot):
    logger.info(f'Отработка callback: {call.data}')
    bot.send_message(call.message.chat.id, TEXT_MESSAGES['test_'], reply_markup=keyboard_for_test())
    bot.set_state(call.message.chat.id, MyStates.test, call.from_user.id)


def callback_survey(call, bot):
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.send_message(call.message.chat.id, TEXT_MESSAGES['survey'])
    bot.set_state(call.message.chat.id, MyStates.name, call.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(call.message.chat.id, call.from_user.id)}')


