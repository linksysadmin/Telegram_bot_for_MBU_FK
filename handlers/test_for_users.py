import logging

from handlers.keyboards import keyboard_question1, keyboard_question2, keyboard_question3, keyboard_question4, \
    keyboard_question5, keyboard_question6, keyboard_question7, keyboard_question8, keyboard_question9, \
    keyboard_question10, remove_keyboard
from services.states import MyStates

logger = logging.getLogger(__name__)


def start_test(message, bot):
    bot.add_data(message.from_user.id, message.chat.id, test_score=0)
    bot.send_message(message.chat.id, '1. Какое число не вписывается в этот ряд?',
                     reply_markup=keyboard_question1())
    bot.set_state(message.chat.id, MyStates.question, message.from_user.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')


def get_answer_to_question(message, bot):
    if message.text in ('9', 'Зеленый', 'Бразилия', 'Иерусалим', 'Спящий', 'Медь', 'Медсестра', 'Круг', 'Лев', 'Ислам'):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['test_score'] = int(data['test_score']) + 1
    if message.text in ('4', '9', '2'):
        bot.send_message(message.chat.id, '2. Какой цвет не вписывается в этот ряд?', reply_markup=keyboard_question2())
    elif message.text in ('Зеленый', 'Желтый', 'Синий'):
        bot.send_message(message.chat.id, '3. Какая страна не вписывается в этот ряд?',
                         reply_markup=keyboard_question3())
    elif message.text in ('Бразилия', 'Канада', 'Мексика'):
        bot.send_message(message.chat.id, '4. Какой город лишний?', reply_markup=keyboard_question4())
    elif message.text in ('Варшава', 'Париж', 'Иерусалим'):
        bot.send_message(message.chat.id, '5. Какое слово лишнее?', reply_markup=keyboard_question5())
    elif message.text in ('Умный', 'Смешной', 'Спящий'):
        bot.send_message(message.chat.id, '6. Какой металл не вписывается в этот ряд?',
                         reply_markup=keyboard_question6())
    elif message.text in ('Серебро', 'Медь', 'Золото'):
        bot.send_message(message.chat.id, '7. Какая профессия не вписывается в этот ряд?',
                         reply_markup=keyboard_question7())
    elif message.text in ('Медсестра', 'Костоправ', 'Хирург'):
        bot.send_message(message.chat.id, '8. Какая геометрическая фигура не вписывается в этот ряд?',
                         reply_markup=keyboard_question8())
    elif message.text in ('Квадрат', 'Круг', 'Треугольник'):
        bot.send_message(message.chat.id, '9. Какое животное не вписывается в этот ряд?',
                         reply_markup=keyboard_question9())
    elif message.text in ('Кенгуру', 'Коала', 'Лев'):
        bot.send_message(message.chat.id, '10. Какая религия не вписывается в этот ряд?',
                         reply_markup=keyboard_question10())
    elif message.text in ('Ислам', 'Иудаизм', 'Буддизм'):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            remove_keyboard(message, bot, f'Тест пройден! Сумма ваших баллов: {data["test_score"]}')
            bot.delete_state(message.from_user.id, message.chat.id)
    logger.info(f'Состояние пользователя - {bot.get_state(message.from_user.id, message.chat.id)}')
