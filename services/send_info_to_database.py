import logging

from sqlite3 import IntegrityError
from services.db import execute, fetch_all

logger = logging.getLogger(__name__)


def check_user_in_database(user_id, direction: str) -> bool:
    result_from_db = fetch_all(
        sql='''SELECT user_id FROM {} WHERE user_id = ?'''.format(direction),
        params=(user_id,)
    )
    return bool(len(result_from_db))


def add_user_data_to_db(direction: str, name: str, date_of_birthday: str,
                        age: int, sex: str, email: str, phone: str, user_id: int):
    try:
        execute(
            sql='''INSERT INTO {} (user_id, name, date_of_birthday, age, sex, email, phone)
                 VALUES (?, ?, ?, ?, ?, ?, ?)'''.format(direction),
            params=(user_id, name, date_of_birthday, age, sex, email, phone))
        return True
    except IntegrityError:
        logger.warning(f'Уже есть этот пользователь в таблице {direction}')
        return False
    except Exception as e:
        logger.error(e)


def update_data(table_name: str, column_name: str, value: (str, int), user_id: int):
    execute(
        sql='''UPDATE {} SET {} = ? WHERE user_id = ?;'''.format(table_name, column_name),
        params=(value, user_id)
    )


if __name__ == '__main__':
    pass
    # add_user_data_to_db('practice', 'Эдуард вкекеыв Звягинцев', '2002-03-23', 21,
    #                     'Мужской', 'ex@csa.com', '+3523523422', 123213212)
    # add_singly_data('practice', 'phone', '+23423423', 123213212)
    # print(check_user_in_database(123213212, 'practice'))
