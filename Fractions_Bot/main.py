import telebot
from telebot import types
import time
import datetime
import math
import random
import sqlite3

bot = telebot.TeleBot('5722699716:AAGykIOB_7HtI-xPMD8sI5KHdTYFt9UNdwI')

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️


#todo: 1. Поменять оформление для умножений, делений по аналогии с суммой.
#todo: 2. Поменять оформление разметки Markdown в делении и умножении
#todo: 3. Фиксить команду разности
#todo: 4. Написание базы данных о пользователях
#todo: 5. Оформляем команду creators, добавить список комманд
#todo: 6. Публикация на хостинге



@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    # region call.data для игры
    if call.data == 'lvl_1':
        M = ['+', '-']
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        s = random.choice(M)
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        bot.send_message(call.message.chat.id, f'Решите пример: `({a}/{b}) {s} ({m}/{n}) = `', parse_mode='Markdown')

        if s == '+':
            NOK = LCM(b, n)

            a = a * (NOK // b)
            m = m * (NOK // n)
            znam = n * (NOK // n)

            r = f'{a + m}/{znam}'

        elif s == '-':
            NOK = LCM(b, n)

            a = a * (NOK // b)
            m = m * (NOK // n)
            znam = n * (NOK // n)

            r = f'{a - m}/{znam}'



        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = message.text
            Markup = types.InlineKeyboardMarkup(row_width=1)
            Markup.add(types.InlineKeyboardButton("Получить ещё пример", callback_data="lvl_1"))
            if x == r:
                bot.send_message(call.message.chat.id, f'Верно! Сменить уровень сложности 👉 /game', parse_mode='Markdown', reply_markup=Markup)
            else:
                bot.send_message(call.message.chat.id, f'Неверно! Попробуйте сменить уровень сложности 👉 /game',
                                 parse_mode='Markdown', reply_markup=Markup)

        bot.register_next_step_handler(call.message, message_input)

    if call.data == 'lvl_2':
        M = ['+', '-', '*', '/']
        a = random.randint(1, 25)
        b = random.randint(1, 25)
        s = random.choice(M)
        m = random.randint(1, 25)
        n = random.randint(1, 25)
        bot.send_message(call.message.chat.id, f'Решите пример: `({a}/{b}) {s} ({m}/{n}) = `', parse_mode='Markdown')

        if s == '+':
            NOK = LCM(b, n)

            a = a * (NOK // b)
            m = m * (NOK // n)
            znam = n * (NOK // n)

            r = f'{a + m}/{znam}'

        elif s == '-':
            NOK = LCM(b, n)

            a = a * (NOK // b)
            m = m * (NOK // n)
            znam = n * (NOK // n)

            r = f'{a - m}/{znam}'

        elif s == '*':
            NOK = LCM(b, n)

            x = a * m
            znam = b * n

            cel = (x) // znam
            ost = (x) % znam

            NOD = math.gcd(ost, znam)

            r = f'{a * m}/{znam}'

        elif s == '/':
            NOK = LCM(b, n)

            x = a * n
            znam = b * m

            cel = (x) // znam
            ost = (x) % znam

            NOD = math.gcd(ost, znam)

            r = f'{x}/{znam}'

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = message.text
            Markup = types.InlineKeyboardMarkup(row_width=1)
            Markup.add(types.InlineKeyboardButton("Получить ещё пример", callback_data="lvl_2"))
            if x == r:
                bot.send_message(call.message.chat.id, f'Верно! Сменить уровень сложности 👉 /game', parse_mode='Markdown', reply_markup=Markup)
            else:
                bot.send_message(call.message.chat.id, f'Неверно! Попробуйте сменить уровень сложности 👉 /game',
                                 parse_mode='Markdown', reply_markup=Markup)

        bot.register_next_step_handler(call.message, message_input)

    if call.data == 'lvl_3':
        M = ['+', '-', '*', '/']
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        s = random.choice(M)
        m = random.randint(1, 50)
        n = random.randint(1, 50)
        bot.send_message(call.message.chat.id, f'Решите пример: `({a}/{b}) {s} ({m}/{n}) = `', parse_mode='Markdown')

        if s == '+':
            NOK = LCM(b, n)

            a = a * (NOK // b)
            m = m * (NOK // n)
            znam = n * (NOK // n)

            r = f'{a + m}/{znam}'

        elif s == '-':
            NOK = LCM(b, n)

            a = a * (NOK // b)
            m = m * (NOK // n)
            znam = n * (NOK // n)

            r = f'{a - m}/{znam}'

        elif s == '*':
            NOK = LCM(b, n)

            x = a * m
            znam = b * n

            cel = (x) // znam
            ost = (x) % znam

            NOD = math.gcd(ost, znam)

            r = f'{a * m}/{znam}'

        elif s == '/':
            NOK = LCM(b, n)

            x = a * n
            znam = b * m

            cel = (x) // znam
            ost = (x) % znam

            NOD = math.gcd(ost, znam)

            r = f'{x}/{znam}'

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            x = message.text
            Markup = types.InlineKeyboardMarkup(row_width=1)
            Markup.add(types.InlineKeyboardButton("Получить ещё пример", callback_data="lvl_3"))
            if x == r:
                bot.send_message(call.message.chat.id, f'Верно! Сменить уровень сложности 👉 /game', parse_mode='Markdown', reply_markup=Markup)
            else:
                bot.send_message(call.message.chat.id, f'Неверно! Попробуйте сменить уровень сложности 👉 /game',
                                 parse_mode='Markdown', reply_markup=Markup)

        bot.register_next_step_handler(call.message, message_input)
    # endregion call.data для первого лвл-а игры



# region Команда GAME
@bot.message_handler(commands=['game'])
def game(message):
    Markup = types.InlineKeyboardMarkup(row_width=1)
    Markup.add(types.InlineKeyboardButton("Лёгкий уровень", callback_data="lvl_1"),
               types.InlineKeyboardButton("Средний уровень", callback_data="lvl_2"),
               types.InlineKeyboardButton("Сложный уровень", callback_data="lvl_3"))
    bot.send_message(message.chat.id, f'Добро пожаловать в наш тренажёр для *счёта правильных и неправильных дробей*. \n\n 🤖 Бот принимает ответы вида: *a/b*\n\nЧем выше уровень, тем больше числа', parse_mode='Markdown', reply_markup=Markup)
# endregion Команда GAME

# region Команда CREATORS
@bot.message_handler(commands=['creators'])
def creators(message):
    bot.send_message(message.chat.id, f'Этот бот был создан нами (student: @yanikam22 and teacher: @ilandroxy) в качестве учебного проекта для ознакомления с библиотекой telebot и закрепления на практике пройденной теории языка python. ', parse_mode='Markdown')
# endregion Команда CREATORS

# region Команда STAT
@bot.message_handler(commands=['stat'])
def stat(message):
    if message.chat.id == 1949653479 or message.chat.id == 1891281816:
        con = sqlite3.connect('my_first.db')
        cur = con.cursor()

        cur.execute(f"SELECT * FROM statistics")
        records = cur.fetchall()
        for row in records:
            message_text = f'id пользователя: {row[0]}\n' \
                           f'username: @{row[1]}\n' \
                           f'first_name: {row[2]}\n' \
                           f'last_name: {row[3]}\n' \
                           f'Последний визит: {row[4]}\n\n' \
                           f'[Написать сообщение](tg://user?id={row[0]})\n\n'
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id,'Похоже у Вас нет права доступа, обратитесь к @yanikam22', parse_mode='Markdown')

# endregion Команда STAT

# region Команда START
@bot.message_handler(commands=['start'])
def start(message):



    ID = message.chat.id
    bot.send_message(message.chat.id, f'Ваш user ID: `{ID}`', parse_mode='Markdown')

    first_name = message.from_user.first_name
    message_text = f'Привет *{first_name}*! Как у тебя дела?\nРады, что ты воспользовался нашим ботом для вычисления обыкновенных дробей 🙏\n\nВоспользуйтесь [ссылкой на теорию](https://skysmart.ru/articles/mathematic/obyknovennye-drobi)'

    con = sqlite3.connect('my_first.db')
    cur = con.cursor()

    cur.execute('''
            CREATE TABLE IF NOT EXISTS statistics(
                id INTEGER,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                data TEXT);
            ''')

    cur.execute(f"SELECT * FROM statistics WHERE id = {message.chat.id}")
    records = cur.fetchone()
    d = time.strftime('%c')

    if records is None:
        cur.execute('INSERT INTO statistics VALUES(?, ?, ?, ?, ?);', (message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, d))

    else:
        cur.execute(f"DELETE FROM players WHERE id = {message.chat.id}")
        cur.execute('INSERT INTO players VALUES(?, ?, ?, ?, ?);', (message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, d))
    con.commit()



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Сумма дробей')
    btn2 = types.KeyboardButton('Разность дробей')
    btn3 = types.KeyboardButton('Умножение дробей')
    btn4 = types.KeyboardButton('Деление дробей')
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, message_text, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)
# endregion Команда START

def LCM(x, y):
    maxi = max(x, y)
    for i in range(maxi, 1000000):
        if i % x == 0 and i % y == 0:
            return i


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()
    get_message_bot = get_message_bot.lower()

    # region Кнопка: Сумма дробей
    if get_message_bot == "сумма дробей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(message.chat.id, 'Введите две дроби и знак операции между ними в формате: `[a/b + m/n]`\n\nгде:', parse_mode='Markdown', reply_markup=markup)
        pic_1 = open('photo/plus.jpg', 'rb')
        bot.send_photo(message.chat.id, pic_1)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                text_message = message.text
                try:
                    M = [i for i in text_message.replace('/', ' ').split()]

                    a = int(M[0])
                    b = int(M[1])
                    s = M[2]
                    m = int(M[3])
                    n = int(M[4])

                    if s == '+':
                        NOK = LCM(b, n)

                        a = a * (NOK // b)
                        m = m * (NOK // n)
                        znam = n * (NOK // n)

                        bot.send_message(message.chat.id, f'Приводим к общему наименьшему знаменателю: *{a}/{znam} {s} {m}/{znam}*', parse_mode='Markdown')

                        bot.send_message(message.chat.id, f'Сложили две дроби: *{a + m}/{znam}*', parse_mode='Markdown')

                        cel = (a + m) // znam
                        ost = (a + m) % znam

                        NOD = math.gcd(ost, znam)

                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        btn1 = types.KeyboardButton('Сумма дробей')
                        btn2 = types.KeyboardButton('Разность дробей')
                        btn3 = types.KeyboardButton('Умножение дробей')
                        btn4 = types.KeyboardButton('Деление дробей')
                        markup.add(btn1, btn2, btn3, btn4)
                        if cel != 0:
                            bot.send_message(message.chat.id, f'Результат арифметического действия: *{cel} ({ost // NOD}/{znam // NOD})*\n\n', parse_mode='Markdown', reply_markup=markup)
                        else:
                            bot.send_message(message.chat.id, f'Результат арифметического действия: *({ost // NOD}/{znam // NOD})*', parse_mode='Markdown', reply_markup=markup)
                    else:
                        bot.send_message(message.chat.id, 'Неверный знак операции! Используйте знак *+*', parse_mode='Markdown')
                except IndexError:
                    bot.send_message(message.chat.id,
                                 f"Ввели недостаточно символов, [подробнее об ошибке](https://ru.stackoverflow.com/questions/1377838/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B0%D1%8E-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-indexerror-list-index-out-of-range-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B5-%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C)",
                                 parse_mode="Markdown", disable_web_page_preview=True)
                except ValueError:
                    bot.send_message(message.chat.id, f"Сначала введите два числа,знак, потом ещё два числа, [подробнее об ошибке](https://pythonim.ru/osnovy/valueerror-python)", parse_mode="Markdown", disable_web_page_preview=True)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton('Сумма дробей')
                btn2 = types.KeyboardButton('Разность дробей')
                btn3 = types.KeyboardButton('Умножение дробей')
                btn4 = types.KeyboardButton('Деление дробей')
                markup.add(btn1, btn2, btn3, btn4)
                bot.send_message(message.chat.id, 'Действие успешно отменено.', reply_markup=markup)

        bot.register_next_step_handler(message, message_input)
    # endregion Кнопка: Сумма дробей

    # region Кнопка: Разность дробей
    if get_message_bot == "разность дробей":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Отменить ⛔')
        markup.add(btn1)
        bot.send_message(message.chat.id, 'Введите две дроби и знак операции между ними в формате: `[a/b - m/n]`', parse_mode='Markdown',reply_markup=markup)
        pic_2 = open('photo/minus.jpg', 'rb')
        bot.send_photo(message.chat.id, pic_2)


        @bot.message_handler(content_types=['text'])
        def message_input(message):
            if message.text != 'Отменить ⛔':
                text_message = message.text
                try:
                    M = [i for i in text_message.replace('/', ' ').split()]

                    a = int(M[0])
                    b = int(M[1])
                    s = M[2]
                    m = int(M[3])
                    n = int(M[4])

                    if s == '-':
                        NOK = LCM(b, n)

                        a = a * (NOK // b)
                        m = m * (NOK // n)
                        znam = n * (NOK // n)

                        bot.send_message(message.chat.id, f'Приводим к общему наименьшему знаменателю: *{a}/{znam} {s} {m}/{znam}*', parse_mode='Markdown')

                        bot.send_message(message.chat.id, f'Вычли две дроби: *{a - m}/{znam}*', parse_mode='Markdown')


                        if a - m < 0:
                            cel = ((a - m) // znam) + 1
                            ost = (abs(a - m) % znam)
                        else:
                            cel = ((a - m) // znam)
                            ost = (a - m) % znam

                        NOD = math.gcd(ost, znam)

                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                        btn1 = types.KeyboardButton('Сумма дробей')
                        btn2 = types.KeyboardButton('Разность дробей')
                        btn3 = types.KeyboardButton('Умножение дробей')
                        btn4 = types.KeyboardButton('Деление дробей')
                        markup.add(btn1, btn2, btn3, btn4)
                        if cel != 0:
                            bot.send_message(message.chat.id, f'Результат арифметического действия: *{cel} ({ost // NOD}/{znam // NOD})*', parse_mode='Markdown', reply_markup=markup)
                        else:
                            bot.send_message(message.chat.id, f'Результат арифметического действия: *({ost // NOD}/{znam // NOD})*', parse_mode='Markdown', reply_markup=markup)
                    else:
                        bot.send_message(message.chat.id, 'Неверный знак операции! Используйте знак *-*', parse_mode='Markdown')
                except IndexError:
                    bot.send_message(message.chat.id,
                                 f"Ввели недостаточно символов, [подробнее об ошибке](https://ru.stackoverflow.com/questions/1377838/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B0%D1%8E-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-indexerror-list-index-out-of-range-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B5-%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C)",
                                 parse_mode="Markdown", disable_web_page_preview=True)
                except ValueError:
                    bot.send_message(message.chat.id,
                                     f"Сначала введите два числа,знак, потом ещё два числа, [подробнее об ошибке](https://pythonim.ru/osnovy/valueerror-python)",
                                     parse_mode="Markdown", disable_web_page_preview=True)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton('Сумма дробей')
                btn2 = types.KeyboardButton('Разность дробей')
                btn3 = types.KeyboardButton('Умножение дробей')
                btn4 = types.KeyboardButton('Деление дробей')
                markup.add(btn1, btn2, btn3, btn4)
                bot.send_message(message.chat.id, 'Действие успешно отменено.', reply_markup=markup)

        bot.register_next_step_handler(message, message_input)
    # endregion Кнопка: Разность дробей

    # region Кнопка: Умножение дробей
    if get_message_bot == "умножение дробей":  # запрос обрабатывает текстовое сообщение умножение дробей
        bot.send_message(message.chat.id, 'Введите две дроби и знак операции между ними в формате: [a b * m n]')  # бот отправляет сообщение по id пользователя

        @bot.message_handler(content_types=['text'])  # функция которая обрабатывает запросы с текстовыми сообщениями
        def message_input(message):  # функция
            text_message = message.text
            try:
                M = [i for i in text_message.split()]

                a = int(M[0])
                b = int(M[1])
                s = M[2]
                m = int(M[3])
                n = int(M[4])

                if s == '*':
                    NOK = LCM(b, n)

                    x = a * m
                    znam = b * n


                    cel = (x) // znam
                    ost = (x) % znam

                    NOD = math.gcd(ost, znam)


                    bot.send_message(message.chat.id, f'Умножили и две дроби: {a * m}/{znam}')

                    if a * m < 0:
                        cel = ((a * m) // znam) + 1
                        ost = -((a * m) % znam)
                    else:
                        cel = (a * m) // znam
                        ost = (a * m) % znam

                    NOD = math.gcd(ost, znam)

                    if cel != 0:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: {cel} ({ost // NOD}/{znam // NOD})')
                    else:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: ({ost // NOD}/{znam // NOD})')
                else:
                    bot.send_message(message.chat.id, 'Неверный знак операции! Используйте знак *')

            except IndexError:
                bot.send_message(message.chat.id,
                             f"Ввели недостаточно символов, [подробнее об ошибке](https://ru.stackoverflow.com/questions/1377838/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B0%D1%8E-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-indexerror-list-index-out-of-range-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B5-%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C)",
                             parse_mode="Markdown", disable_web_page_preview=True)
            except ValueError:
                bot.send_message(message.chat.id,
                                 f"Сначала введите два числа,знак, потом ещё два числа, [подробнее об ошибке](https://pythonim.ru/osnovy/valueerror-python)",
                                 parse_mode="Markdown", disable_web_page_preview=True)
        bot.register_next_step_handler(message, message_input)
    # endregion Кнопка: Умножение дробей

    # region Кнопка: Деление дробей
    if get_message_bot == "деление дробей":  # запрос обрабатывает текстовое сообщение умножение дробей
        bot.send_message(message.chat.id, 'Введите две дроби и знак операции между ними в формате: [a b / m n]')  # бот отправляет сообщение по id пользователя

        @bot.message_handler(content_types=['text'])  # функция которая обрабатывает запросы с текстовыми сообщениями
        def message_input(message):  # функция
            text_message = message.text
            try:
                M = [i for i in text_message.split()]

                a = int(M[0])
                b = int(M[1])
                s = M[2]
                m = int(M[3])
                n = int(M[4])

                if s == '/':
                    NOK = LCM(b, n)

                    x = a * n
                    znam = b * m


                    cel = (x) // znam
                    ost = (x) % znam

                    NOD = math.gcd(ost, znam)


                    bot.send_message(message.chat.id, f'Умножили и две дроби: {x}/{znam}')

                    if x < 0:
                        cel = ((x) // znam) + 1
                        ost = -((x) % znam)
                    else:
                        cel = (x) // znam
                        ost = (x) % znam

                    NOD = math.gcd(ost, znam)

                    if cel != 0:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: {cel} ({ost // NOD}/{znam // NOD})')
                    else:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: ({ost // NOD}/{znam // NOD})')
                else:
                    bot.send_message(message.chat.id, 'Неверный знак операции! Используйте знак *')

            except IndexError:
                bot.send_message(message.chat.id,
                             f"Ввели недостаточно символов, [подробнее об ошибке](https://ru.stackoverflow.com/questions/1377838/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B0%D1%8E-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-indexerror-list-index-out-of-range-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B5-%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C)",
                             parse_mode="Markdown", disable_web_page_preview=True)
            except ValueError:
                bot.send_message(message.chat.id,
                                 f"Сначала введите два числа,знак, потом ещё два числа, [подробнее об ошибке](https://pythonim.ru/osnovy/valueerror-python)",
                                 parse_mode="Markdown", disable_web_page_preview=True)

        bot.register_next_step_handler(message, message_input)
    # endregion Кнопка: Деление дробей

    # region Кнопка: Отменить ⛔
    elif get_message_bot == 'отменить ⛔':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Сумма дробей')
        btn2 = types.KeyboardButton('Разность дробей')
        btn3 = types.KeyboardButton('Умножение дробей')
        btn4 = types.KeyboardButton('Деление дробей')
        markup.add(btn1, btn2, btn3, btn4)

        bot.send_message(message.chat.id, 'Действие успешно отменено.', parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup)
    # endregion: Кнопка: Отменить ⛔

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)