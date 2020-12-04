# coding: utf8
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
import time
import random
from datetime import datetime
import json
import requests
import emoji
import regex
 
login = input('-----------------------------------------\nPlease input your vk login: ')
password = input('-----------------------------------------\nPlease input your vk password: ')
try:
  app_id = input(int('-----------------------------------------\nPlease input your vk id: '))
except:
  print('error')
vk_session = vk_api.VkApi(login=login, password=password, app_id=app_id)
vk_session.auth(token_only=True)
 
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment})


count = 0
counter = 0
count1 = 0
counter1 = 0
mes = 0
prog = False
 
print('Started')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text.lower()
        response2 = event.text
        checker = [response]
        if event.from_user:
            if checker[0].split(" ")[0] == "комент":
                count = 0
                counter = 0
                count1 = 0
                counter1 = 0
                mes = 0
                prog = True
                try:
                    response = response2.split()[1:]
                    textt = '_'.join(response)
                    find = ('https://api.remanga.org/api/activity/comments/?chapter_id=' + str(textt) + '&chapter_page=-1')
                    resp = requests.get(find)
                    resp = str(resp.text)
                    a = json.loads(resp.replace("'",'"'))
                    counter = len(a['content'][0])
                    while True:
                        if mes >= 10:
                            mes = 0
                            print('sleep')
                            send_message(vk_session, 'peer_id', event.peer_id, message = '{Анти-Капча} Остановка на 60 секунд')
                            time.sleep(60)
                        send_message(vk_session, 'peer_id', event.peer_id, message = 'Аватарка: ' + 'remanga.org/media/users/' + str(a['content'][count]['user']['id']) + '/avatar.jpg\n' + 'Профиль: ' + 'remanga.org/user/' + str(a['content'][count]['user']['id']) + '\n' + a['content'][count]['user']['username'] + ': ' + a['content'][count]['text'])
                        mes += 1
                        count += 1
                        print(count1, counter1, count, counter, mes)
                        time.sleep(1)
                    count = 0
                    counter = 0
                except Exception as err:
                    send_message(vk_session, 'peer_id', event.peer_id, message = 'Если коментарий выглядит странно, значит бот не смог декодировать его\nСкорее всего воспроизведение закончилось ' + str(err)) 
            if checker[0].split(" ")[0] == "глава":
                count = 0
                counter = 0
                count1 = 0
                counter1 = 0
                mes = 0
                prog = True
                try:
                    response = response2.split()[1:]
                    textt = '_'.join(response)
                    find = ('https://api.remanga.org/api/titles/chapters/' + str(textt))
                    resp = requests.get(find)
                    resp = str(resp.text)
                    a = json.loads(resp.replace("'",'"'))
                    counter1 = len(a['content']['pages'][0])
                    send_message(vk_session, 'peer_id', event.peer_id, message = 'Информация: \nТом: ' + str(a['content']['tome']) + '\nГлава: ' + str(a['content']['chapter']) + '\nНазвание главы: ' + str(a['content']['name']))
                    try:
                        while count1 <= counter1:
                            counter = len(a['content']['pages'][count1][0])
                            while count <= counter:
                                if mes >= 10:
                                    mes = 0
                                    print('sleep')
                                    send_message(vk_session, 'peer_id', event.peer_id, message = '{Анти-Капча} Остановка на 60 секунд')
                                    time.sleep(60)
                                print(count1, counter1, count, counter, mes)
                                send_message(vk_session, 'peer_id', event.peer_id, message = a['content']['pages'][count1][count]['link'])
                                mes += 1
                                count += 1
                                time.sleep(1)
                            count1 += 1
                            count = 0
                            prog = False
                    except Exception as err:
                        print(spical_for_error)
                except:
                    try:
                        response = response2.split()[1:]
                        textt = '_'.join(response)
                        find = ('https://api.remanga.org/api/titles/chapters/' + str(textt))
                        resp = requests.get(find)
                        resp = str(resp.text)
                        a = json.loads(resp.replace("'",'"'))
                        counter = len(a['content']['pages'][0])
                        while True:
                            if mes >= 10:
                                mes = 0
                                print('sleep')
                                send_message(vk_session, 'peer_id', event.peer_id, message = '{Анти-Капча} Остановка на 60 секунд')
                                time.sleep(60)
                            send_message(vk_session, 'peer_id', event.peer_id, message = a['content']['pages'][count]['link'])
                            mes += 1
                            count += 1
                            print(count1, counter1, count, counter, mes)
                            time.sleep(1)
                        count = 0
                        counter = 0
                    except Exception as err:
                        send_message(vk_session, 'peer_id', event.peer_id, message = 'Скорее всего воспроизведение закончилось ' + str(err)) 
 
        if event.from_chat:
            if checker[0].split(" ")[0] == "комент":
                count = 0
                counter = 0
                count1 = 0
                counter1 = 0
                mes = 0
                prog = True
                try:
                    response = response2.split()[1:]
                    textt = '_'.join(response)
                    find = ('https://api.remanga.org/api/activity/comments/?chapter_id=' + str(textt) + '&chapter_page=-1')
                    resp = requests.get(find)
                    resp = str(resp.text)
                    a = json.loads(resp.replace("'",'"'))
                    counter = len(a['content'][0])
                    while True:
                        if mes >= 10:
                            mes = 0
                            print('sleep')
                            send_message(vk_session, 'peer_id', event.peer_id, message = '{Анти-Капча} Остановка на 60 секунд')
                            time.sleep(60)
                        send_message(vk_session, 'peer_id', event.peer_id, message = 'Аватарка: ' + 'remanga.org/media/users/' + str(a['content'][count]['user']['id']) + '/avatar.jpg\n' + 'Профиль: ' + 'remanga.org/user/' + str(a['content'][count]['user']['id']) + '\n' + a['content'][count]['user']['username'] + ': ' + a['content'][count]['text'])
                        mes += 1
                        count += 1
                        print(count1, counter1, count, counter, mes)
                        time.sleep(1)
                    count = 0
                    counter = 0
                except Exception as err:
                    send_message(vk_session, 'peer_id', event.peer_id, message = 'Если коментарий выглядит странно, значит бот не смог декодировать его\nСкорее всего воспроизведение закончилось ' + str(err)) 
            if checker[0].split(" ")[0] == "глава":
                count = 0
                counter = 0
                count1 = 0
                counter1 = 0
                mes = 0
                prog = True
                try:
                    response = response2.split()[1:]
                    textt = '_'.join(response)
                    find = ('https://api.remanga.org/api/titles/chapters/' + str(textt))
                    resp = requests.get(find)
                    resp = str(resp.text)
                    a = json.loads(resp.replace("'",'"'))
                    counter1 = len(a['content']['pages'][0])
                    send_message(vk_session, 'peer_id', event.peer_id, message = 'Информация: \nТом: ' + str(a['content']['tome']) + '\nГлава: ' + str(a['content']['chapter']) + '\nНазвание главы: ' + str(a['content']['name']))
                    try:
                        while count1 <= counter1:
                            counter = len(a['content']['pages'][count1][0])
                            while count <= counter:
                                if mes >= 10:
                                    mes = 0
                                    print('sleep')
                                    send_message(vk_session, 'peer_id', event.peer_id, message = '{Анти-Капча} Остановка на 60 секунд')
                                    time.sleep(60)
                                print(count1, counter1, count, counter, mes)
                                send_message(vk_session, 'peer_id', event.peer_id, message = str(a['content']['pages'][count1][count]['link']))
                                mes += 1
                                count += 1
                                time.sleep(1)
                            count1 += 1
                            count = 0
                            prog = False
                    except Exception as err:
                        print(error)
                except:
                    try:
                        response = response2.split()[1:]
                        textt = '_'.join(response)
                        find = ('https://api.remanga.org/api/titles/chapters/' + str(textt))
                        resp = requests.get(find)
                        resp = str(resp.text)
                        a = json.loads(resp.replace("'",'"'))
                        counter = len(a['content']['pages'][0])
                        while True:
                            if mes >= 10:
                                mes = 0
                                print('sleep')
                                send_message(vk_session, 'peer_id', event.peer_id, message = '{Анти-Капча} Остановка на 60 секунд')
                                time.sleep(60)
                            send_message(vk_session, 'peer_id', event.peer_id, message = a['content']['pages'][count]['link'])
                            mes += 1
                            count += 1
                            print(count1, counter1, count, counter, mes)
                            time.sleep(1)
                        count = 0
                        counter = 0
                    except Exception as err:
                        send_message(vk_session, 'peer_id', event.peer_id, message = 'Скорее всего воспроизведение закончилось ' + str(err)) 
