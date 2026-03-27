import telebot
from telebot import types
import datetime
import requests

API_TOKEN = '5999635405:AAH3etiW_ZBEBeQVTB4nyRPXue2cld2bLEg'
crypto_bot = telebot.TeleBot(API_TOKEN)
#chat_id=-1001826708302

op_id_list = [638772675, 1239902124]

def send_message_to_op(text):
    try:
        for j in op_id_list:
            crypto_bot.send_message(j, text)
    except:
        print("Ошибка отправления сообщения операторам.")

def add_user(id, pl_time):
    try:
        file = open('db.txt', 'a+')
        file.close()
        file = open('db.txt', 'r')
        text = file.read()
        file.close()

        #if not text.find(str(id)) == -1:
        #    return crypto_bot.send_message(message_g.chat.id, 'Пользователь уже есть в базе данных.')
        db_outside = text.split('\n')[:-1]
        db_inside = []
        db_id_list = []
        for i in range(len(db_outside)):
            db_inside.append(db_outside[i].split(' : '))
            db_id_list.append(int(db_inside[i][0]))
        if id in db_id_list: return crypto_bot.send_message(message_g.chat.id, '[Ex11] Пользователь уже есть в базе данных.')

        # print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
        year = int(datetime.datetime.utcnow().strftime('%Y'))
        month = int(datetime.datetime.utcnow().strftime('%m'))
        day = int(datetime.datetime.utcnow().strftime('%d'))
        hour = int(datetime.datetime.utcnow().strftime('%H'))
        minute = int(datetime.datetime.utcnow().strftime('%M'))
        # print(year, month, day, hour, minute)
        # print()

        unitime = 738880
        if year - 2023 > 0:
            for i in range(1, year - 2023 + 1):
                year_d = 365
                if i % 4 == 0:
                    if i % 100 == 0:
                        if i % 400 == 0:
                            year_d = 366
                        year_d = 365
                    else:
                        year_d = 366
                else:
                    year_d = 365
                unitime += year_d

        year_d = 365
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    year_d = 366
                year_d = 365
            else:
                year_d = 366
        else:
            year_d = 365

        for i in range(1, month + 1):
            month_d = 31
            if i == 1:
                month_d = 31
            elif i == 2:
                if year_d == 365:
                    month_d = 28
                else:
                    month_d = 29
            elif i == 3:
                month_d = 31
            elif i == 4:
                month_d = 30
            elif i == 5:
                month_d = 31
            elif i == 6:
                month_d = 30
            elif i == 7:
                month_d = 31
            elif i == 8:
                month_d = 31
            elif i == 9:
                month_d = 30
            elif i == 10:
                month_d = 31
            elif i == 11:
                month_d = 30
            elif i == 12:
                month_d = 31
            unitime += month_d

        # ------------------------------------------------
        unitime = (unitime + day) * 24 * 60 + hour * 60 + minute
        unitime_i = unitime + pl_time

        time = unitime_i
        # ------------------------------------------------

        now_time = datetime.datetime.utcnow()
        now_time += datetime.timedelta(minutes=pl_time)
        time_visual = now_time.strftime('%Y-%m-%d %H:%M') + ' (UTC time)'

        response = requests.get(f'https://api.telegram.org/bot{API_TOKEN}/getChat?chat_id={id}')
        username = "ERROR WITH GETTING USERNAME"
        first_name = "ERROR WITH GETTING FIRST NAME"
        last_name = "ERROR WITH GETTING LAST NAME"
        if response.status_code == 200:
            user_data = response.json()['result']
            username = user_data.get('username')
            first_name = user_data.get('first_name')
            last_name = user_data.get('last_name')

        file = open('db.txt', 'w')
        try:
            file.write(text + str(id) + ' : ' + str(time) + ' : ' + str(time_visual) + ' : @' + str(username) + ' : (' + str(first_name) + ' : ' + str(last_name) + ")\n")
        except:
            try:
                file.write(text + str(id) + ' : ' + str(time) + ' : ' + str(time_visual) + ' : @' + str(username) + ' : (')
                #....
                for i in str(first_name):
                    file.close()
                    file = open('db.txt', 'r')
                    temp_text = file.read()
                    file.close()
                    file = open('db.txt', 'w')
                    try:
                        file.write(temp_text + i)
                    except:
                        file.write(temp_text + '?')
                file.close()
                file = open('db.txt', 'r')
                temp_text = file.read()
                file.close()
                file = open('db.txt', 'w')
                file.write(temp_text + ' : ')
                for i in str(last_name):
                    file.close()
                    file = open('db.txt', 'r')
                    temp_text = file.read()
                    file.close()
                    file = open('db.txt', 'w')
                    try:
                        file.write(temp_text + i)
                    except:
                        file.write(temp_text + '?')
                file.close()
                file = open('db.txt', 'r')
                temp_text = file.read()
                file.close()
                file = open('db.txt', 'w')
                file.write(temp_text + ')\n')
            except:
                try:
                    file.write(text + str(id) + ' : ' + str(time) + ' : ' + str(time_visual) + ' : @' + str(username) + ' : (?unk_firstname? : ?unk_lastname:?)\n')
                except:
                    file.write(text)
                    crypto_bot.send_message(message_g.chat.id, '[Ex15] Возникла ошибка добавления пользователя. Проверьте целостность базы данных или правильность введённых данных.')

        file.close()
        crypto_bot.send_message(message_g.chat.id, 'Пользователь успешно добавлен!')
        send_message_to_op(f'----------------------------\nДобавлен пользователь с ID: {int(id)}\nUsername(tag): @{str(username)}\nFirst name: {str(first_name)}\nLast name: {str(last_name)}\nTime: {pl_time} minutes\nEnd-time: {str(time_visual)}\nUni-end-time: {time}\n----------------------------')
        try:
            inv_link = crypto_bot.create_chat_invite_link(-1001826708302, str(id), datetime.datetime.utcnow() + datetime.timedelta(minutes=180 + 180), 1, False)
            crypto_bot.send_message(message_g.chat.id, f'Одноразовая ссылка на вступление в канал: {inv_link.invite_link} (действительна в течении трёх часов).')
            crypto_bot.send_message(message_g.chat.id, '⬆️ Перешлите сообщение выше добавленному пользователю. ️')
        except:
            crypto_bot.send_message(message_g.chat.id, '[Ex16] Возникла ошибка создания пригласительной ссылки. Добавьте пользователя в канал вручную.')
    except:
        crypto_bot.send_message(message_g.chat.id, '[Ex12] Возникла ошибка добавления пользователя. Проверьте целостность базы данных или правильность введённых данных.')

def del_user(id):
    try:
        file = open('db.txt', 'a+')
        file.close()
        file = open('db.txt', 'r')
        text = file.read()
        file.close()

        #if text.find(str(id)) == -1:
        #    return crypto_bot.send_message(message_g.chat.id, 'Пользователь отсутствует в базе данных.')
        db_outside = text.split('\n')[:-1]
        db_inside = []
        db_id_list = []
        for i in range(len(db_outside)):
            db_inside.append(db_outside[i].split(' : '))
            db_id_list.append(int(db_inside[i][0]))
        if id not in db_id_list: return crypto_bot.send_message(message_g.chat.id, '[Ex13] Пользователь отсутствует в базе данных.')
        username = db_outside[db_id_list.index(id)].split(' : ')[3]

        db_outside.remove(db_outside[db_id_list.index(id)])
        text = '\n'.join(db_outside) + '\n'

        #text = text[:text.find(str(id))] + text[text.find(str(id)):][text[text.find(str(id)):].find('\n')+1:]
        file = open('db.txt', 'w')
        file.write(text)
        file.close()
        crypto_bot.send_message(message_g.chat.id, 'Пользователь успешно удалён из базы данных!')
        send_message_to_op(f'----------------------------\nУдалён пользователь с ID: {id}\nUsername(tag): {username}\n----------------------------')
        try:
            crypto_bot.kick_chat_member(chat_id=-1001826708302, user_id=int(id))
            crypto_bot.send_message(message_g.chat.id, 'Пользователь успешно удалён с канала!')
        except:
            crypto_bot.send_message(message_g.chat.id, '[Ex17] Возникла ошибка удаления пользователя из канала. Удалите его вручную.')
        try:
            crypto_bot.unban_chat_member(chat_id=-1001826708302, user_id=int(id))
        except:
            crypto_bot.send_message(message_g.chat.id, '[Ex18] Возникла ошибка исключения пользователя из чёрного списка сервера. Исключите его оттуда вручную.')
    except:
        crypto_bot.send_message(message_g.chat.id, '[Ex14] Возникла ошибка удаления пользователя. Проверьте целостность базы данных или правильность введённых данных.')

def print_db():
    file = open('db.txt', 'r')
    text = file.read()
    file.close()
    text = 'User ID : Uni-end-time : End-time : User tag : (First name : Second name)\n' + text
    text1 = text
    pl_n = 0
    for i in range(len(text)):
        if text[i] == '\n':
            text1 = text1[:i+pl_n] + '\n' + text1[i+pl_n:]
            pl_n += 1
    crypto_bot.send_message(message_g.chat.id, text1)
    
# Handle '/start' and '/help'
#@crypto_bot.message_handler(commands=['help', 'start'])
#def send_welcome(message):
#    crypto_bot.reply_to(message, "Hi there, I am EchoBot.\nI am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@crypto_bot.message_handler(func=lambda message: True)
@crypto_bot.message_handler(content_types=['text'])
def main_message(message):
    if not message.from_user.id in op_id_list: return crypto_bot.send_message(message.from_user.id, "You have no permission to use me.")
    global message_g
    message_g = message
    try:
        if message.text.lstrip().rstrip()[:(message.text.lstrip().rstrip()+' ').find(' ')] == "/m" or message.text.lstrip().rstrip()[:(message.text.lstrip().rstrip()+' ').find(' ')] == "/help" or message.text.lstrip().rstrip()[:(message.text.lstrip().rstrip()+' ').find(' ')] == "/start":
            keyboard = types.InlineKeyboardMarkup()
            key_add_user = types.InlineKeyboardButton(text='Добавить пользователя', callback_data='add_user')
            keyboard.add(key_add_user)
            key_del_user = types.InlineKeyboardButton(text='Удалить пользователя', callback_data='del_user')
            keyboard.add(key_del_user)
            key_print_db = types.InlineKeyboardButton(text='Вывести базу данных', callback_data='print_db')
            keyboard.add(key_print_db)
            crypto_bot.send_message(message.from_user.id, text="Список комманд бота:\n\n1. /add_user [user id(можно узнать через @userinfobot)] [Время доступа в минутах]\n2. /del_user [user id(можно узнать через @userinfobot)]\n3. /print_db\n\nИли просто тыкни по нужной кнопочке снизу ⬇️", reply_markup=keyboard)
        elif message.text.lstrip().rstrip()[:(message.text.lstrip().rstrip()+' ').find(' ')] == "/add_user" and len(list(message.text.lstrip().rstrip().split()))==3:
            try:
                txt1 = (message.text.lstrip().rstrip()+' ')[(message.text.lstrip().rstrip()+' ').find(' ')+1:]+' '
            except: return crypto_bot.send_message(message.from_user.id, "[Ex2] Неверная комманда.")
            try:
                id1 = int(txt1[:txt1.find(' ')])
            except: return crypto_bot.send_message(message.from_user.id, "[Ex3] Неверно указан ID пользователя.")
            try:
                if int(txt1[txt1.find(' ')+1:].rstrip()) > 0:
                    time1 = int(txt1[txt1.find(' ')+1:].rstrip())
                else: id1 = int('')
            except: return crypto_bot.send_message(message.from_user.id, "[Ex4] Неверно указано время.")
            add_user(id1,time1)
        elif message.text.lstrip().rstrip()[:(message.text.lstrip().rstrip() + ' ').find(' ')] == "/del_user" and len(list(message.text.lstrip().rstrip().split())) == 2:
            try:
                txt1 = (message.text.lstrip().rstrip()+' ')[(message.text.lstrip().rstrip()+' ').find(' ')+1:]+' '
            except: return crypto_bot.send_message(message.from_user.id, "[Ex5] Неверная комманда.")
            try:
                id1 = int(txt1[:txt1.find(' ')])
            except: return crypto_bot.send_message(message.from_user.id, "[Ex6] Неверно указан ID пользователя.")
            del_user(id1)
        elif message.text.lstrip().rstrip()[:(message.text.lstrip().rstrip() + ' ').find(' ')] == "/print_db":
            print_db()
        else:
            crypto_bot.send_message(message.from_user.id, "[Ex7] Неверная комманда.")
    except:
        crypto_bot.send_message(message.from_user.id, "[Ex1] Неверная комманда.")

def get_id(message):
    global message_g
    message_g = message
    try:
        global id
        id = int(message.forward_from.id)
        crypto_bot.send_message(message.chat.id, 'Введите время доступа для этого пользователя(в минутах):')
        crypto_bot.register_next_step_handler(message, get_time)
    except:
        crypto_bot.send_message(message.chat.id, '[Ex8] Упс! Что-то пошло не так. Возможно вы переслали сообщение с какого-то чата или у пользователя скрыт профиль. Перепроверьте введённые вами данные, если всё правильно то попробуйте узнать ID пользователя с помощью @userdatabot и добавить его вручную через /add_user.')

def get_time(message):
    global message_g
    message_g = message
    try:
        global time
        time = int(message.text.lstrip().rstrip())
        if time <= 0: time = int('')
        add_user(id,time)
    except:
        crypto_bot.send_message(message.chat.id, '[Ex9] Упс! Что-то пошло не так. Проверьте правильность введённых данных и повторите попытку.')
    crypto_bot.register_next_step_handler(message, main_message)

def get_id_del(message):
    global message_g
    message_g = message
    try:
        global id
        id = int(message.forward_from.id)
        del_user(id)
    except:
        crypto_bot.send_message(message.chat.id, '[Ex10] Упс! Что-то пошло не так. Возможно вы переслали сообщение с какого-то чата или у пользователя скрыт профиль. Перепроверьте введённые вами данные, если всё правильно то попробуйте узнать ID пользователя с помощью @userdatabot и удалить его вручную через /del_user.')
    crypto_bot.register_next_step_handler(message, main_message)



@crypto_bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "add_user":
        crypto_bot.send_message(call.message.chat.id, 'Перешлите мне любое сообщение от этого пользователя.')
        crypto_bot.register_next_step_handler(message_g, get_id)
    if call.data == "del_user":
        crypto_bot.send_message(call.message.chat.id, 'Перешлите мне любое сообщение от этого пользователя.')
        crypto_bot.register_next_step_handler(message_g, get_id_del)
    if call.data == "print_db":
        print_db()

if __name__ == "__main__":
    crypto_bot.infinity_polling()