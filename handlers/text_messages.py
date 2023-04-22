import logging

logging.getLogger(__name__)

TEXT_MESSAGES = {
    'start': "Привет <b>{username}</b>!, я бот-помощник по стажировке в МБУ ФК, тут есть вся нужна информация, "
             "которая может помочь тебе.\nЕсли тебя заинтересует, то оставляй свою анкету ;)",

    'info': "🎗 Программа практики для студентов 2-3 курса бакалавриата/специалитета\n\n"
            "✅ Предназначена для обучающихся по направлениям: бухгалтерский учет и аудит, экономика, государственное "
            "и муниципальное управление, IT и иным, после прохождения тестирования\n\n"
            "✅ Направления практики: бухгалтерский (бюджетный) учет и отчетность, IT, оплата труда и иные выплаты\n\n"
            "✅ Продолжительность программы: от 4 недель\n\n"
            '✅ На практике студенты получат представление о функциональных возможностях подсистем ГИИС "Электронный '
            'бюджет", пройдут интерактивное обучение в облачном портале и получат практические знания в '
            'специализированной учебной лаборатории.\n\n'
            '✅ По итогам прохождения практики студенты научатся анализировать данные, работать в режиме '
            'многозадачности, а также получат возможность перехода в программу "Старт с МБУ".\n\n'
            '/start - Меню\n/test - Пройти тестирование\n/survey - Пройти анкетирование\n'
            '/resume - Отправить резюме\n/university - Выбрать ВУЗ\n/season - Выбрать период\n'
            '/info_personal_reception - Информация о личном приёме граждан\n/feedback - Обратная связь',

    'test_': 'Для того, чтобы пройти тест Вам нужно ответить на вопросы, вы готовы ?\n\n'
             '/start - Меню',

    'survey': 'Выберите направление: стажировка или практика.\n\n'
              '/start - Меню',

    'resume': 'Отправьте ваш файл с резюме\n\n'
              '/start - Меню',

    'university': 'Выберите ВУЗ из списка:\n\n1. Ранхигс\n2. Финунивер\n3. РГГУ\n4. РУТ МИИТ\n5. ГУУ\n6. МИРЭА\n7.'
                  'МИСИС\n8. РУДН\n9. РЭУ им. Плеханова\n10. ВАВТ\n11. МЭИ\n\n'
                  '/start - Меню',

    'season': "Выберите период:\n\nВесна, Лето, Осень, Зима\n\n"
              "/start - Меню",

    'info_personal_reception': "Личный прием граждан и организаций:\n\n"
                               "Харций Марианна Михайловна\nРуководитель Межрегионального бухгалтерского УФК\nпервый вторник месяца\n10:00 - 12:00\n\n"
                               "Князькова Наталья Сергеевна\nЗаместитель руководителя Межрегионального бухгалтерского УФК\nвторой вторник месяца\n10:00 - 12:00\n\n"
                               "Соломатин Дмитрий Владимирович\nЗаместитель руководителя Межрегионального бухгалтерского УФК\nтретий вторник месяца\n10:00 - 12:00\n\n"
                               "Бузунов Антон Сергеевич\nЗаместитель руководителя Межрегионального бухгалтерского УФК\nчетвёртый вторник месяца\n10:00 - 12:00\n\n"
                               "Исаев Магомед Хусейнович\nЗаместитель руководителя Межрегионального бухгалтерского УФК\nвторой вторник месяца\n13:00-14:00\n\n"
                               "/start - Меню\n/test - Пройти тестирование\n/survey - Пройти анкетирование\n"
                               "/resume - Отправить резюме\n/university - Выбрать ВУЗ\n/season - Выбрать период\n"
                               "/info_personal_reception - Информация о личном приёме граждан\n/feedback - Обратная связь",

    'feedback': "Обратная связь:\n\n"
                "Начальник отдела:\nТоноян Грант Егишевич\ngtonoyan@roskazna.ru\n\n"
                "Главный специалист-эксперт:\nЗапылихин Владислав Сергеевич\nvzapylihin@roskazna.ru\n\n"
                "Ведущий специалист-эксперт:\nХрановская Светлана Александровна\nshranovskaya@roskazna.ru\n\n"
                "/start - Меню\n/test - Пройти тестирование\n/survey - Пройти анкетирование\n"
                "/resume - Отправить резюме\n/university - Выбрать ВУЗ\n/season - Выбрать период\n"
                "/info_personal_reception - Информация о личном приёме граждан\n/feedback - Обратная связь",
}
