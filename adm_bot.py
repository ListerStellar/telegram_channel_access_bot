import telebot
import datetime
#from main import add_user
#from main import del_user
#chat_id=-1001826708302
API_TOKEN = '5999635405:AAH3etiW_ZBEBeQVTB4nyRPXue2cld2bLEg'
bot = telebot.TeleBot(API_TOKEN)
op_id_list = [638772675, 1239902124]

def get_unitime():
    year = int(datetime.datetime.utcnow().strftime('%Y'))
    month = int(datetime.datetime.utcnow().strftime('%m'))
    day = int(datetime.datetime.utcnow().strftime('%d'))
    hour = int(datetime.datetime.utcnow().strftime('%H'))
    minute = int(datetime.datetime.utcnow().strftime('%M'))
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
    unitime = (unitime + day) * 24 * 60 + hour * 60 + minute
    return unitime

# for i in db_id_list:
#     try:
#         chat_info = bot.get_chat_member(-1001826708302, i)
#         print(f"Статус пользователя с id {i}: {chat_info.status}")
#     except:
#         print(f"Пользователь с id {i} отсутствует на канале.")

#bot.kick_chat_member(chat_id=-1001826708302, user_id=5072868639)
#bot.unban_chat_member(chat_id=-1001826708302, user_id=5072868639)
#print(bot.create_chat_invite_link(-1001826708302, "asfdase", datetime.datetime.utcnow()+datetime.timedelta(minutes=180+10), 1, False))
#print(bot.revoke_chat_invite_link(-1001826708302, "https://t.me/+b7qG1GEN86hmNGUy"))

def send_message_to_op(text):
    try:
        for j in op_id_list:
            bot.send_message(j, text)
    except:
        print("Ошибка отправления сообщения операторам.")

def del_user(id):
    try:
        send_message_to_op("----------------------------")
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
        if id not in db_id_list:
            for j in op_id_list:
                bot.send_message(j, '[Ex13] Пользователь отсутствует в базе данных.')
                return 0x13

        db_outside.remove(db_outside[db_id_list.index(id)])
        text = '\n'.join(db_outside) + '\n'

        #text = text[:text.find(str(id))] + text[text.find(str(id)):][text[text.find(str(id)):].find('\n')+1:]
        file = open('db.txt', 'w')
        file.write(text)
        file.close()
        send_message_to_op('Пользователь успешно удалён из базы данных!')
        try:
            bot.kick_chat_member(chat_id=-1001826708302, user_id=int(id))
            send_message_to_op('Пользователь успешно удалён с канала!')
        except:
            send_message_to_op('[Ex17] Возникла ошибка удаления пользователя из канала. Удалите его вручную.')
        try:
            bot.unban_chat_member(chat_id=-1001826708302, user_id=int(id))
        except:
            send_message_to_op('[Ex18] Возникла ошибка исключения пользователя из чёрного списка сервера. Исключите его оттуда вручную.')
    except:
        send_message_to_op('[Ex14] Возникла ошибка удаления пользователя. Проверьте целостность базы данных или правильность введённых данных.')


once = True
once_count = True
while True:
    if int(datetime.datetime.utcnow().strftime('%M'))%2==0:
        if once:
            once = False
            # ------------------------------
            file = open('db.txt', 'a+')
            file.close()
            file = open('db.txt', 'r')
            text = file.read()
            file.close()
            db_outside = text.split('\n')[:-1]
            db_inside = []
            db_id_list = []
            for i in range(len(db_outside)):
                db_inside.append(db_outside[i].split(' : '))
                db_id_list.append(int(db_inside[i][0]))

            db_members_status = []
            r_unitime = get_unitime()
            for i in db_inside:
                ifdel = r_unitime >= int(i[1])
                try:
                    chat_info = bot.get_chat_member(-1001826708302, int(i[0]))
                    db_members_status.append([chat_info.status, ifdel, int(i[0]), i[3]])
                    #print(f"Статус пользователя с id {i[3]}: {chat_info.status}")
                except:
                    db_members_status.append(['leave', ifdel, int(i[0])])
                    #print(f"Пользователь с id {i[3]} отсутствует на канале.")
            # for i in range(len(db_members_status)):
            #     if not (db_members_status[i][0] == 'administrator' or db_members_status[i][0] == 'creator' or db_members_status[i][0] == 'member'):
            #         del_user(int(db_members_status[i][2]))
            #         send_message_to_op("Deleted user with ID " + str(db_members_status[i][2]) + ', ' + str(db_members_status[i][3]))
            #         send_message_to_op("----------------------------")
            print()
            print(db_members_status)
            print()
            # print(len(db_inside), bot.get_chat_member_count(-1001826708302) - 1)

            for i in range(len(db_members_status)):
                if db_members_status[i][1] == True:
                    del_user(db_members_status[i][2])
                    send_message_to_op("Deleted user with ID "+str(db_members_status[i][2])+', '+str(db_members_status[i][3]))
                    send_message_to_op("----------------------------")
                    #print("Deleted user with ID", db_members_status[i][2], ',', db_members_status[i][3])
            try:
                if not int(len(db_inside)) == int(bot.get_chat_member_count(-1001826708302) - 1):
                    if once_count:
                        send_message_to_op(f'----------------------------\n❗ Замечено расхождение в количестве участников сервера и их количеством в базе данных! ❗\nБД: {int(len(db_inside))}\nCервер: {int(bot.get_chat_member_count(-1001826708302) - 1)}\n----------------------------')
                        once_count = False
                else:
                    once_count = True
            except:
                print('Ошибка проверки количества пользователей (БД/Сервер).')
            # ------------------------------
    else:
        once = True
