import telebot
from telebot import types
import datetime
import pendulum
import csv
token = '6944176491:AAFutBEeym_NGP6p0gWx5_rGr_65FeglEE8'
bot = telebot.TeleBot(token)


markup = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Часть 1')
btn2 = types.KeyboardButton('Часть 2')
markup.row(btn1, btn2)
btn3 = types.KeyboardButton('Часть 3')
btn4 = types.KeyboardButton('Часть 4')
markup.row(btn3, btn4)
btn5 = types.KeyboardButton('Посмотреть мои ответы')
markup.row(btn5)
btn6 = types.KeyboardButton('Завершить')
markup.row(btn6)


markup2 = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('1')
btn2 = types.KeyboardButton('2')
btn3 = types.KeyboardButton('3')
btn4 = types.KeyboardButton('4')
btn5 = types.KeyboardButton('5')
markup2.row(btn1, btn2, btn3, btn4, btn5)
btn6 = types.KeyboardButton('Назад')
markup2.row(btn6)

markup3 = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('6')
btn2 = types.KeyboardButton('7')
btn3 = types.KeyboardButton('8')
btn4 = types.KeyboardButton('9')
btn5 = types.KeyboardButton('10')
markup3.row(btn1, btn2, btn3, btn4, btn5)
btn6 = types.KeyboardButton('Назад')
markup3.row(btn6)

markup4 = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('11')
btn2 = types.KeyboardButton('12')
btn3 = types.KeyboardButton('13')
btn4 = types.KeyboardButton('14')
btn5 = types.KeyboardButton('15')
markup4.row(btn1, btn2, btn3, btn4, btn5)
btn6 = types.KeyboardButton('Назад')
markup4.row(btn6)

markupch1 = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('1')
btn2 = types.KeyboardButton('2')
btn3 = types.KeyboardButton('3')
btn4 = types.KeyboardButton('4')
markupch1.row(btn1, btn2, btn3, btn4)
btn6 = types.KeyboardButton('Назад')
markupch1.row(btn6)

markupn = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Назад')
markupn.row(btn1)

markupyn = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('да')
btn2 = types.KeyboardButton('нет')
markupyn.row(btn1, btn2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, команда ВЭШ рада приветствовать тебя на нашем пробном региональном"
                                      " этапе! \n\nМы очень надеемся, что тебе понравятся задачи, которые мы подготовили "
                                      "для тебя! Для начала давай создадим уникальный никнейм.  По нему ты сможешь"
                                      " узнать свое место в рейтинге среди написавших. Если ты не хочешь, чтобы твой"
                                      " результат увидели другие участники, ты всегда можешь создать случайный ник,"
                                      " по которому никто не сможет тебя идентифицировать (например monsterkill2005)."
                                      " Все оскорбительные никнеймы будут удалены.\n В случае возникновения технических"
                                      " неполадок используй /help. Если это не помогло решить проблему,"
                                      " напиши Роме (@raamensavin).")
    bot.register_next_step_handler(message, nick)


def nick(message):
    if message.text[0] == '/' or len(message.text) > 30:
        bot.send_message(message.chat.id, "Некорректное имя попробуйте другое")
        bot.register_next_step_handler(message, nick)
    else:
        a = 0
        with open('nicks.csv', "r") as fin:
            re = csv.reader(fin)
            at = []
            for row in re:
                at += row
            if at.count(message.text) != 0:
                bot.send_message(message.chat.id, "Занят, выберите другой")
                bot.register_next_step_handler(message, nick)
            else:
                a = 1
        if a == 1:
            with open('nicks.csv', "a") as fin:
                writer = csv.writer(fin)
                usr = [message.from_user.id, message.from_user.username, message.text]
                writer.writerow(usr)
                bot.send_message(chat_id='726382042', text=f"{message.from_user.username} зарегался как {message.text}")
                #bot.send_document(message.chat.id, open('Пробный Муницип.pdf', "rb"))
                msg = bot.send_message(message.chat.id, f"Очень приятно, {message.text}, для продолжения укажи, пожалуйста"
                                                  f", ФИО, почту, регион обучения (в каком городе школа), и класс обуче"
                                                  f"ния через запятую. В формате: 'Рома Савин, romashka@gmail.com, "
                                                  f"Москва, 13'.")
                bot.register_next_step_handler(msg, fio)


def fio(message):
    if len(message.text.split(',')) != 4:
        bot.send_message(message.chat.id, 'Какая-то проблема в формате, попробуй перечитать инструкцию к формату.')
        bot.register_next_step_handler(message, fio)
    else:
        if message.text.split(',')[1].count('@') == 0:
            bot.send_message(message.chat.id, 'Какая-то проблема в формате, попробуй перечитать инструкцию к формату.')
            bot.register_next_step_handler(message, fio)
        else:
            with open('imena.csv', "a") as fin:
                writer = csv.writer(fin)
                ussr = message.text.split(',') + [f'{message.from_user.username}']
                writer.writerow(ussr)
            bot.send_message(message.chat.id, 'Супер, все готово, для приступления к сдаче задач используй /region.\n'
                                              'Сразу после отправки команды пойдет время, а именно 3 часа на решение за'
                                              'дачек и 10 минут на загрузку, всего 190 минут. По истечении данного време'
                                              'ни возможности сдать задания не будет.')


@bot.message_handler(commands=['region'])
def ziza(message):
    a = 0
    with open('time.csv', 'r') as fin:
        rid = csv.reader(fin)
        for row in rid:
            if int(row[0]) == int(message.from_user.id):
                a = 1
    if a == 0:
        bot.send_document(message.chat.id, open('probreg.pdf', "rb"))
        with open('time.csv', 'a') as fin:
            writer = csv.writer(fin)
            usr = [message.from_user.id, message.from_user.username, datetime.datetime.now()+datetime.timedelta(minutes=190)]
            writer.writerow(usr)
        bot.send_message(message.chat.id, text=f'Сейчас - {pendulum.now().format("HH:mm:ss")}, конец - {(pendulum.now().add(minutes=190)).format("HH:mm:ss")}'
                                               f'\n\n\nВыберите часть:', reply_markup=markup)
        bot.register_next_step_handler(message, click)
    else:
        bot.send_message(message.chat.id, 'Вы уже начали, выберите часть:', reply_markup=markup)
        bot.register_next_step_handler(message, click)


def click(message):
    if message.text.lower() == 'часть 1':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ.', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.lower() == 'часть 2':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. \n'
                                                'Отправьте варианты ответов, которые вы выбрали без пробелов (например,'
                                                ' если вы выбрали 1), 2) и 4) напишите 124)', reply_markup=markup3)
        bot.register_next_step_handler(msg, ch2)
    elif message.text.lower() == 'часть 3':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ.', reply_markup=markup4)
        bot.register_next_step_handler(msg, ch3)
    elif message.text.lower() == 'часть 4':
        msg = bot.send_message(message.chat.id, 'Пришлите ОДИН pdf файл с вашим решением 4 части, файлы разбитые на нес'
                                                'колько фотографий или документов или в другом формате'
                                                ' обработаны не будут и, к сожалению, мы не сможем'
                                                ' их проверить. Для создания одного файла можно использовать онлайн серви'
                                                'сы, такие как ilovepdf.com.', reply_markup=markupn)
        bot.register_next_step_handler(msg, ch4)
    elif message.text.lower() == 'посмотреть мои ответы':
        a = 0
        usi = []
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                if int(row[0]) == int(message.from_user.id):
                    a = 1
                    usi.append(row)
        if a == 0:
            bot.send_message(message.chat.id, 'Вы не сдали ни одной задачи')
            bot.register_next_step_handler(message, click)
        else:
            bot.send_message(message.chat.id, f'Ваши ответы: {usi[0][2]} {usi[0][3]} {usi[0][4]} {usi[0][5]} {usi[0][6]} {usi[0][7]} '
                                              f'{usi[0][8]} {usi[0][9]} {usi[0][10]} {usi[0][11]} {usi[0][12]} {usi[0][13]} '
                                              f'{usi[0][14]} {usi[0][15]} {usi[0][16]}')
            bot.register_next_step_handler(message, click)
    elif message.text.lower() == 'завершить':
        a = 0
        usi = []
        with open ('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                if int(row[0]) == int(message.from_user.id):
                    a = 1
                    usi.append(row)
        if a == 0:
            bot.send_message(message.chat.id, 'Вы не сдали ни одной задачи')
            bot.register_next_step_handler(message, click)
        else:
            bot.send_message(message.chat.id,
                             f'Ваши ответы: {usi[0][2]} {usi[0][3]} {usi[0][4]} {usi[0][5]} {usi[0][6]} {usi[0][7]} '
                             f'{usi[0][8]} {usi[0][9]} {usi[0][10]} {usi[0][11]} {usi[0][12]} {usi[0][13]} '
                             f'{usi[0][14]} {usi[0][15]} {usi[0][16]}')
            msg = bot.send_message(message.chat.id, 'Вы уверены, что хотите закончить?', reply_markup=markupyn)
            bot.register_next_step_handler(msg, check)
    else:
        msg = bot.send_message(message.chat.id, 'Используйте кнопки')
        bot.register_next_step_handler(msg, click)


def check(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Понравилось? Присоединяйся к другим нашим проектам: \n1. Воскресным контестам'
                                          ' от ВЭШ, которые ты можешь найти по ссылке: https://t.me/contest_vesh \n2. '
                                          'Нашему интенсиву к региональному этапу ВСОШ по Экономике. Больше информации '
                                          'можно найти по ссылке: https://t.me/v_e_sh/567. А также следи за результатами'
                                          ' в нашем основном канале!!'
                                          ' До скорых встреч!', reply_markup=types.ReplyKeyboardRemove())
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, text='Выберите часть:', reply_markup=markup)
        bot.register_next_step_handler(message, click)
    else:
        bot.send_message(message.chat.id, text='Что-то не так, используйте кнопки.', reply_markup=markup2)
        bot.register_next_step_handler(message, check)


def ch1(message):
    with open('time.csv', 'r') as fin:
        rid = csv.reader(fin)
        for row in rid:
            if int(row[0]) == int(message.from_user.id):
                titi = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
    if datetime.datetime.now() > titi:
        bot.send_message(message.chat.id, 'Время вышло, отправленные ответы обработаны, но новые отправить нельзя.')
    else:
        if message.text == '1':
            msg1 = bot.send_message(message.chat.id, 'Выберите ваш ответ на 1 номер:', reply_markup=markupch1)
            bot.register_next_step_handler(msg1, ch11)
        elif message.text == '2':
            msg1 = bot.send_message(message.chat.id, 'Выберите ваш ответ на 2 номер:', reply_markup=markupch1)
            bot.register_next_step_handler(msg1, ch12)
        elif message.text == '3':
            msg1 = bot.send_message(message.chat.id, 'Выберите ваш ответ на 3 номер:', reply_markup=markupch1)
            bot.register_next_step_handler(msg1, ch13)
        elif message.text == '4':
            msg1 = bot.send_message(message.chat.id, 'Выберите ваш ответ на 4 номер:', reply_markup=markupch1)
            bot.register_next_step_handler(msg1, ch14)
        elif message.text == '5':
            msg1 = bot.send_message(message.chat.id, 'Выберите ваш ответ на 5 номер:', reply_markup=markupch1)
            bot.register_next_step_handler(msg1, ch15)
        elif message.text.lower() == 'назад':
            bot.send_message(message.chat.id, text='Выберите часть:', reply_markup=markup)
            bot.register_next_step_handler(message, click)


def ch11(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a = 1
                    num = c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[2] = message.text
            A.append(usr)
        else:
            usr[2] = message.text
            A[num] = usr
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup2)
        bot.register_next_step_handler(message, ch1)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch11)


def ch12(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[3] = message.text
            A.append(usr)
        else:
            usr[3] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup2)
        bot.register_next_step_handler(message, ch1)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch12)


def ch13(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[4] = message.text
            A.append(usr)
        else:
            usr[4] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup2)
        bot.register_next_step_handler(message, ch1)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch13)


def ch14(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[5] = message.text
            A.append(usr)
        else:
            usr[5] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup2)
        bot.register_next_step_handler(message, ch1)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch14)


def ch15(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[6] = message.text
            A.append(usr)
        else:
            usr[6] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup2)
        bot.register_next_step_handler(message, ch1)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch15)


def ch2(message):
    with open('time.csv', 'r') as fin:
        rid = csv.reader(fin)
        for row in rid:
            if int(row[0]) == int(message.from_user.id):
                titi = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
    if datetime.datetime.now() > titi:
        bot.send_message(message.chat.id, 'Время вышло, отправленные ответы обработаны, но новые отправить нельзя.')
    else:
        if message.text == '6':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 6 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch21)
        elif message.text == '7':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 7 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch22)
        elif message.text == '8':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 8 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch23)
        elif message.text == '9':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 9 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch24)
        elif message.text == '10':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 10 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch25)
        elif message.text.lower() == 'назад':
            bot.send_message(message.chat.id, text='Выберите часть:', reply_markup=markup)
            bot.register_next_step_handler(message, click)


def ch21(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a = 1
                    num = c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[7] = message.text
            A.append(usr)
        else:
            usr[7] = message.text
            A[num] = usr
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup3)
        bot.register_next_step_handler(message, ch2)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch21)


def ch22(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[8] = message.text
            A.append(usr)
        else:
            usr[8] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup3)
        bot.register_next_step_handler(message, ch2)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch22)


def ch23(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[9] = message.text
            A.append(usr)
        else:
            usr[9] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup3)
        bot.register_next_step_handler(message, ch2)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch23)


def ch24(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[10] = message.text
            A.append(usr)
        else:
            usr[10] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup3)
        bot.register_next_step_handler(message, ch2)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch24)


def ch25(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[11] = message.text
            A.append(usr)
        else:
            usr[11] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup3)
        bot.register_next_step_handler(message, ch2)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch25)


def ch3(message):
    with open('time.csv', 'r') as fin:
        rid = csv.reader(fin)
        for row in rid:
            if int(row[0]) == int(message.from_user.id):
                titi = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
    if datetime.datetime.now() > titi:
        bot.send_message(message.chat.id, 'Время вышло, отправленные ответы обработаны, но новые отправить нельзя.')
    else:
        if message.text == '11':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 11 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch31)
        elif message.text == '12':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 12 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch32)
        elif message.text == '13':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 13 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch33)
        elif message.text == '14':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 14 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch34)
        elif message.text == '15':
            msg1 = bot.send_message(message.chat.id, 'Введите ваш ответ на 15 номер:', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch35)
        elif message.text.lower() == 'назад':
            bot.send_message(message.chat.id, text='Выберите часть:', reply_markup=markup)
            bot.register_next_step_handler(message, click)


def ch31(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a = 1
                    num = c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[12] = message.text
            A.append(usr)
        else:
            usr[12] = message.text
            A[num] = usr
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup4)
        bot.register_next_step_handler(message, ch3)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch31)


def ch32(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[13] = message.text
            A.append(usr)
        else:
            usr[13] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup4)
        bot.register_next_step_handler(message, ch3)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch32)


def ch33(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[14] = message.text
            A.append(usr)
        else:
            usr[14] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup4)
        bot.register_next_step_handler(message, ch3)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch33)


def ch34(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[15] = message.text
            A.append(usr)
        else:
            usr[15] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup4)
        bot.register_next_step_handler(message, ch3)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch34)


def ch35(message):
    if message.text.lower() == 'назад':
        msg = bot.send_message(message.chat.id, 'Выберите номер, на который хотите сдать ответ. Сдавайте '
                                                'номера ответа, а не сам ответ (например, если вы выбрали 1)0.5, то нап'
                                                'ишите 1 без скобки)', reply_markup=markup2)
        bot.register_next_step_handler(msg, ch1)
    elif message.text.isdigit():
        A = []
        usr = [0] * 17
        a = 0
        c = 0
        num1 = 0
        with open('ribyata.csv', 'r') as fin:
            rid = csv.reader(fin)
            for row in rid:
                A.append(row)
                if int(row[0]) == int(message.from_user.id):
                    usr = row
                    a += 1
                    num1 += c
                c += 1
        if a == 0:
            usr[0] = message.from_user.id
            with open('nicks.csv', 'r') as fin:
                rid = csv.reader(fin)
                for row in rid:
                    if int(row[0]) == int(message.from_user.id):
                        nickk = row[2]
            usr[1] = nickk
            usr[16] = message.text
            A.append(usr)
        else:
            usr[16] = message.text
            A[num1] = usr
        with open('ribyata.csv', 'w') as f:
            f.write('')
        with open('ribyata.csv', 'w') as fin:
            wri = csv.writer(fin)
            for i in A:
                wri.writerow(i)
        bot.send_message(message.chat.id, 'Записано, выбери следующий номер, если хочешь изменить ответ выбери номер еще'
                                          ' раз.', reply_markup=markup4)
        bot.register_next_step_handler(message, ch3)
    else:
        bot.send_message(message.chat.id, 'Что-то не так, отправьте другой ответ')
        bot.register_next_step_handler(message, ch35)


def ch4(message):
    with open('time.csv', 'r') as fin:
        rid = csv.reader(fin)
        for row in rid:
            if int(row[0]) == int(message.from_user.id):
                titi = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S.%f')
    if datetime.datetime.now() > titi:
        bot.send_message(message.chat.id, 'Время вышло, отправленные ответы обработаны, но новые отправить нельзя.')
    else:
        if message.photo is not None:
            msg1 = bot.send_message(message.chat.id, 'Это фотография а не файл, отправьте файл.', reply_markup=markupn)
            bot.register_next_step_handler(msg1, ch4)
        elif message.document is not None:
            if message.document.file_name.endswith('.pdf'):
                bot.forward_message('726382042', message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Принято, для того, чтоб отправить другой файл выберите эту часть еще раз'
                                                  ', проверен будет только последний отправленный файл. Вы можете выбра'
                                                  'ть другую часть или завершить работу.', reply_markup=markup)
                bot.register_next_step_handler(message, click)
            else:
                msg1 = bot.send_message(message.chat.id, 'Это не pdf, попробуйте еще раз', reply_markup=markupn)
                bot.register_next_step_handler(msg1, ch4)
        else:
            if message.text.lower() == 'назад':
                bot.send_message(message.chat.id, text='Выберите часть:', reply_markup=markup)
                bot.register_next_step_handler(message, click)
            else:
                msg1 = bot.send_message(message.chat.id, 'Это не файл, отправьте решение все развернутые решения 4 части'
                                                         ' одним файлом', reply_markup=markupn)
                bot.register_next_step_handler(msg1, ch4)
    
@bot.message_handler(commands=['help'])
def help_m(message):
    bot.send_message(message.chat.id, 'После создания ника и заполнения ваших данных, вы должны были получить файл с за'
                                      'даниями, если этого не произошло, свяжитесь с Ромой @raamensavin. После получения'
                                      ' задач используйте /region для сдачи ответов. Внимательно прочитайте инструкцию по'
                                      'формату ответов и всем удачи!!')


bot.infinity_polling()
