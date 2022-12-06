import telebot
from telebot import types
import time
import math
import random

bot = telebot.TeleBot('5722699716:AAGykIOB_7HtI-xPMD8sI5KHdTYFt9UNdwI')

# 👉 🙏 👆 👇 😅 👋 🙌 ☺️ ❗ ️‼️ ✌️ 👌 ✊ 👨‍💻  🤖 😉  ☝️ ❤️ 💪 ✍️ 🎯  ⛔  ️✅ 📊📈🧮   🗳️

#todo: 1. Поменять оформление для умножений, делений по аналогии с суммой.
#todo: 2. Поменять оформление разметки Markdown в делении и умножении
#todo: 3. Фиксить команду разности
#todo: 4. Развиваем игру тренировку /game
#todo: 5. Делаем команду preview о проекте


@bot.callback_query_handler(func=lambda call: True)
def step(call):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    if call.data == 'key':
        pass

# region Команда GAME
@bot.message_handler(commands=['game'])
def game(message):
    M = ['+', '-', '*', '/']
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    s = random.choice(M)
    m = random.randint(1, 10)
    n = random.randint(1, 10)
    bot.send_message(message.chat.id, f'Решите пример: `{a}/{b} {s} {m}/{n} = `', parse_mode='Markdown')

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
        if x == r:
            bot.send_message(message.chat.id, f'Верно, еще пример 👉 /game', parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, f'Неверно! попробуйте еще один пример 👉 /game', parse_mode='Markdown')

    bot.register_next_step_handler(message, message_input)


# region Команда START
@bot.message_handler(commands=['start'])
def start(message):
    ID = message.chat.id
    bot.send_message(message.chat.id, f'Ваш user ID: `{ID}`', parse_mode='Markdown')

    first_name = message.from_user.first_name
    message_text = f'Привет *{first_name}*! Как у тебя дела?\nРады, что ты воспользовался нашим ботом для вычисления обыкновенных дробей 🙏\n\nВоспользуйтесь [ссылкой на теорию](https://skysmart.ru/articles/mathematic/obyknovennye-drobi)'

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
        bot.send_message(message.chat.id, 'Введите две дроби и знак операции между ними в формате: `[a/b + m/n]`\n\nгде:', parse_mode='Markdown')
        pic_1 = open('photo/plus.jpg', 'rb')
        bot.send_photo(message.chat.id, pic_1)

        @bot.message_handler(content_types=['text'])
        def message_input(message):
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

                    if cel != 0:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: *{cel} ({ost // NOD}/{znam // NOD})*\n\n', parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: *({ost // NOD}/{znam // NOD})*', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, 'Неверный знак операции! Используйте знак *+*', parse_mode='Markdown')
            except IndexError:
                bot.send_message(message.chat.id,
                             f"Ввели недостаточно символов, [подробнее об ошибке](https://ru.stackoverflow.com/questions/1377838/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B0%D1%8E-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-indexerror-list-index-out-of-range-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B5-%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C)",
                             parse_mode="Markdown", disable_web_page_preview=True)
            except ValueError:
                bot.send_message(message.chat.id, f"Сначала введите два числа,знак, потом ещё два числа, [подробнее об ошибке](https://pythonim.ru/osnovy/valueerror-python)", parse_mode="Markdown", disable_web_page_preview=True)

        bot.register_next_step_handler(message, message_input)
    # endregion Кнопка: Сумма дробей

    # region Кнопка: Разность дробей
    if get_message_bot == "разность дробей":
        bot.send_message(message.chat.id, 'Введите две дроби и знак операции между ними в формате: `[a/b - m/n]`', parse_mode='Markdown')
        pic_2 = open('photo/minus.jpg', 'rb')
        bot.send_photo(message.chat.id, pic_2)


        @bot.message_handler(content_types=['text'])
        def message_input(message):
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

                    if cel != 0:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: *{cel} ({ost // NOD}/{znam // NOD})*', parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id, f'Результат арифметического действия: *({ost // NOD}/{znam // NOD})*', parse_mode='Markdown')
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



if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            print(e)