from bs4 import BeautifulSoup
import datetime
import time
import requests
from config import token

def get_offset(group_id):
    params = {'access_token': token, 'group_id': group_id, 'v': 5.131}
    r = requests.get('https://api.vk.com/method/groups.getMembers', params=params)
    count = r.json()['response']['count']
    print(f'Количество подписчиков: {count}')
    if count > 1000:
        return count // 1000
    else:
        count = 1
        return count

def get_users(group_id, from_data):
    """Получаем всех участников группы и фильтруем от неактивных"""
    active_users = []
    un_active_list = []
    for offset in range(0, get_offset(group_id)+1):
        params = {'access_token': token, 'v': 5.131, 'group_id': group_id, 'offset': offset*1000, 'fields': 'last_seen'}
        users = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()['response']
        for user in users['items']:
            start_point_data = datetime.datetime.strptime(from_data, '%d.%m.%Y').timestamp()
            try:
                if user['last_seen']['time'] >= start_point_data:
                    active_users.append({'id': user['id'], 'name': user['first_name'] + ' ' + user['last_name'], 'likes': user['likes']['count'], 'reposts': user['reposts']['count'], 'comments': user['comments']['count']})
                else:
                    un_active_list.append(user['id'])
            except:
                continue
    active_users.sort(key=lambda x: x['likes'] + x['reposts'] + x['comments'], reverse=True)
    return active_users[:3]

def parser(group_list):
    from_data = input('Введите дату, с которой хотите отслеживать активность\nформат: дд.мм.гггг: ')
    print(f'Анализируем с {from_data}\n')
    for group in group_list:
        print(f'Группа: {group}')
        try:
            top_users = get_users(group, from_data=from_data)
            print('Топ-3 самых активных пользователей:')
            for user in top_users:
                print(f'ID: {user["id"]}, Имя: {user["name"]}, Лайки: {user["likes"]}, Репосты: {user["reposts"]}, Комментарии: {user["comments"]}')
            time.sleep(2)
        except Exception as ex:
            print(f'{group} - не предвиденная ошибка: {ex}\n')
            continue

if __name__ == '__main__':
    group_list = [...] #указать айди необходимой группы(можно несколько)
    parser(group_list)
