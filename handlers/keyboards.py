from telebot import types


def keyboard_enter_menu():
    """Keyboard for main menu"""
    keyboard = types.InlineKeyboardMarkup(row_width=True)
    key1 = types.InlineKeyboardButton(text='Общая информация о стажировках/практиках',
                                      callback_data='info')
    key2 = types.InlineKeyboardButton(text='Первичный (пройти) тест', callback_data='test')
    key3 = types.InlineKeyboardButton(text='Анкета', callback_data='survey')
    key4 = types.InlineKeyboardButton(text='Прикрепить резюме', callback_data='resume')
    key5 = types.InlineKeyboardButton(text='ВУЗ', callback_data='university')
    key6 = types.InlineKeyboardButton(text='Период', callback_data='season')
    key7 = types.InlineKeyboardButton(text='Личный прием граждан и организаций',
                                      callback_data='info_about_personal_reception')
    key8 = types.InlineKeyboardButton(text='Получение обратной связи', callback_data='feedback')
    key9 = types.InlineKeyboardButton(text='Виртуальная экскурсия', url='https://youtu.be/0_mvah21iIU')
    keyboard.add(key1, key2, key3, key4, key5, key6, key7, key8, key9)
    return keyboard


def keyboard_for_test():
    """Keyboard for questions"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Да, пройти тест')
    key2 = types.KeyboardButton(text='Нет')
    keyboard.add(key1, key2)
    return keyboard


def keyboard_sex():
    """ Keyboard for choice the sex """
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Мужской')
    key2 = types.KeyboardButton(text='Женский')
    keyboard.add(key1, key2)
    return keyboard


def keyboard_send_phone():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    send_phone_button = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    cancel_button = types.KeyboardButton(text="Отменить")
    keyboard.add(send_phone_button, cancel_button)
    return keyboard


def keyboard_consent_to_send_data():
    """Keyboard for consent to send data"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Отправить')
    key2 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2)
    return keyboard


def keyboard_yes_or_no():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Да')
    key2 = types.KeyboardButton(text='Нет')
    key3 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3)
    return keyboard


def keyboard_university():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='1. Ранхиг')
    key2 = types.KeyboardButton(text='2. Финунивер')
    key3 = types.KeyboardButton(text='3. РГГУ')
    key4 = types.KeyboardButton(text='4. РУТ МИИТ')
    key5 = types.KeyboardButton(text='5. ГУУ')
    key6 = types.KeyboardButton(text='6. МИРЭА')
    key7 = types.KeyboardButton(text='7. МИСИС')
    key8 = types.KeyboardButton(text='8. РУДН')
    key9 = types.KeyboardButton(text='9. РЭУ им. Плеханова')
    key10 = types.KeyboardButton(text='10. ВАВТ')
    key11 = types.KeyboardButton(text='11. МЭИ')
    key12 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12)
    return keyboard


def keyboard_question1():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='4')
    key2 = types.KeyboardButton(text='9')
    key3 = types.KeyboardButton(text='2')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question2():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Зеленый')
    key2 = types.KeyboardButton(text='Желтый')
    key3 = types.KeyboardButton(text='Синий')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question3():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Бразилия')
    key2 = types.KeyboardButton(text='Канада')
    key3 = types.KeyboardButton(text='Мексика')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question4():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Варшава')
    key2 = types.KeyboardButton(text='Париж')
    key3 = types.KeyboardButton(text='Иерусалим')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question5():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Умный')
    key2 = types.KeyboardButton(text='Смешной')
    key3 = types.KeyboardButton(text='Спящий')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question6():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Серебро')
    key2 = types.KeyboardButton(text='Медь')
    key3 = types.KeyboardButton(text='Золото')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question7():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Медсестра')
    key2 = types.KeyboardButton(text='Костоправ')
    key3 = types.KeyboardButton(text='Хирург')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question8():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Квадрат')
    key2 = types.KeyboardButton(text='Круг')
    key3 = types.KeyboardButton(text='Треугольник')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question9():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Кенгуру')
    key2 = types.KeyboardButton(text='Коала')
    key3 = types.KeyboardButton(text='Лев')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


def keyboard_question10():
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    key1 = types.KeyboardButton(text='Ислам')
    key2 = types.KeyboardButton(text='Иудаизм')
    key3 = types.KeyboardButton(text='Буддизм')
    key4 = types.KeyboardButton(text='Отменить')
    keyboard.add(key1, key2, key3, key4)
    return keyboard


# REMOVE KEYBOARD
def remove_keyboard(message, bot, text: str) -> None:
    bot.send_message(message.chat.id, f'{text}',
                     reply_markup=types.ReplyKeyboardRemove())
