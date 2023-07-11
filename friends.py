# # from bs4 import BeautifulSoup
# # import datetime
# # import time
# # import requests
# # from config import token

# # def get_offset(group_id):
# #     params = {'access_token': token, 'group_id': group_id, 'v': 5.131}
# #     r = requests.get('https://api.vk.com/method/groups.getMembers', params=params)
# #     count = r.json()['response']['count']
# #     print(f'Количество подписчиков: {count}')
# #     if count > 1000:
# #         return count // 1000
# #     else:
# #         count = 1
# #         return count

# # def get_users(group_id, from_data):
# #     """Получаем всех участников группы и фильтруем от неактивных"""
# #     active_users = []
# #     un_active_list = []
# #     for offset in range(0, get_offset(group_id)+1):
# #         params = {'access_token': token, 'v': 5.131, 'group_id': group_id, 'offset': offset*1000, 'fields': 'last_seen'}
# #         users = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()['response']
# #         for user in users['items']:
# #             start_point_data = datetime.datetime.strptime(from_data, '%d.%m.%Y').timestamp()
# #             try:
# #                 if user['last_seen']['time'] >= start_point_data:
# #                     active_users.append({'id': user['id'], 'name': user['first_name'] + ' ' + user['last_name'], 'likes': user['likes']['count'], 'reposts': user['reposts']['count'], 'comments': user['comments']['count']})
# #                 else:
# #                     un_active_list.append(user['id'])
# #             except:
# #                 continue
# #     active_users.sort(key=lambda x: x['likes'] + x['reposts'] + x['comments'], reverse=True)
# #     return active_users[:3]

# # def parser(group_list):
# #     from_data = input('Введите дату, с которой хотите отслеживать активность\nв формате: дд.мм.гггг: ')
# #     print(f'Анализируем с {from_data}\n')
# #     for group in group_list:
# #         print(f'Группа: {group}')
# #         try:
# #             top_users = get_users(group, from_data=from_data)
# #             print('Топ-3 самых активных пользователей:')
# #             for user in top_users:
# #                 print(f'id: {user["id"]}, Имя: {user["name"]}, Лайки: {user["likes"]}, Репосты: {user["reposts"]}, Комментарии: {user["comments"]}')
# #             time.sleep(2)
# #         except Exception as ex:
# #             print(f'{group} - не предвиденная ошибка: {ex}\n')
# #             continue

# # if __name__ == '__main__':
# #     group_list = ['sashashlapick'] #указать айди необходимой группы(можно несколько)
# #     parser(group_list)


# # from bs4 import BeautifulSoup
# # import datetime
# # import time
# # import requests
# # from config import token

# # def get_offset(group_id):
# #     params = {'access_token': token, 'group_id': group_id, 'v': 5.131}
# #     r = requests.get('https://api.vk.com/method/groups.getMembersCount', params=params)
# #     count = r.json().get('response', 0)
# #     print(f'Количество подписчиков: {count}')
# #     if count > 1000:
# #         return count // 1000
# #     else:
# #         count = 1
# #         return count

# # def get_users(group_id, from_data):
# #     """Получаем всех участников группы и фильтруем от неактивных"""
# #     active_users = []   
# #     un_active_list = []
# #     for offset in range(0, get_offset(group_id)+1):
# #         params = {'access_token': token, 'v': 5.131, 'group_id': group_id, 'offset': offset*1000, 'fields': 'last_seen'}
# #         try:
# #             response = requests.get('https://api.vk.com/method/groups.getMembers', params=params).json()
# #             users = response.get('response', {}).get('items', [])
# #             for user in users:
# #                 start_point_data = datetime.datetime.strptime(from_data, '%d.%m.%Y').timestamp() + 86400                
# #                 try:
# #                     if user['last_seen']['time'] > start_point_data:
# #                         active_users.append({'id': user['id'], 'name': user['first_name'] + ' ' + user['last_name'], 'likes': user.get('likes', {}).get('count', 0), 'reposts': user.get('reposts', {}).get('count', 0), 'comments': user.get('comments', {}).get('count', 0)})
# #                     else:
# #                         un_active_list.append(user['id'])
# #                 except:
# #                     continue
# #         except Exception as ex:
# #             print(f'Ошибка при получении данных: {ex}')
# #             continue
# #     active_users.sort(key=lambda x: x.get('likes', 0) + x.get('reposts', 0) + x.get('comments', 0), reverse=True)
# #     return active_users[:3]

# # def parser(group_list):
# #     from_data = input('Введите дату, с которой хотите отслеживать активность\nв формате: дд.мм.гггг: ')
# #     print(f'Анализируем с {from_data}\n')
# #     for group in group_list:
# #         print(f'Группа: {group}')
# #         try:
# #             top_users = get_users(group, from_data=from_data)
# #             print('Топ-3 самых активных пользователей:')
# #             for user in top_users:
# #                 print(f'id: {user["id"]}, Имя: {user["name"]}, Лайки: {user["likes"]}, Репосты: {user["reposts"]}, Комментарии: {user["comments"]}')
# #             time.sleep(2)
# #         except Exception as ex:
# #             print(f'{group} - не предвиденная ошибка: {ex}\n')
# #             continue

# # if __name__ == '__main__':
# #     group_list = ['public177979552'] #указать айди необходимой группы(можно несколько)
# #     parser(group_list)

import requests
from bs4 import BeautifulSoup

access_token = "vk1.a.RFExX1QVm5mbHcHjbl3JaeO2un81YbZVLGpMCP7kSkX4RJk7-kqJm6IdY3ZMqoXbDNCEzUUvguWJ8mHpe-uA7OllLbmt-AUpzNq5qyo3plyU9VRRqPuVkPvkC-mtCRuWRifQGlvKvuCyvo6WfIxNNEBq3yAEghjhmoNdyGnBUeeUUmqEOtomkYAISkiW2xuFbPBTBX9ixATEWkWzBoY2mw"
user_id = "6121396"

def get_user_id(access_token):
    params = {
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.get', params=params)
    user_id = response.json()['response'][0]['id']
    return user_id

def get_active_friends(access_token):
    user_id = get_user_id(access_token)
    params = {
        'access_token': access_token,
        'user_id': user_id,
        'fields': 'friends',
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    active_friends = response.json()['response']['items']
    return active_friends

def get_user_info(user_id, access_token):
    params = {
        'user_ids': user_id,
        'fields': 'counters',
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.get', params=params).json()
    
    if 'response' in response and isinstance(response['response'], list) and len(response['response']) > 0:
        user_info = response['response'][0]
        return user_info
    else:
        return {}

def get_top_active_friends(access_token):
    friend_ids = get_active_friends(access_token)
    top_active_friends = []
    
    for friend_id in friend_ids:
        friend_info = get_user_info(friend_id, access_token)
        
        if friend_info is not None:
            counters = friend_info.get('counters', {})
            total_count = counters.get('likes', 0) + counters.get('comments', 0) + counters.get('reposts', 0)
            top_active_friends.append((friend_id, total_count))
    
    top_active_friends.sort(key=lambda x: x[1], reverse=True)
    return top_active_friends[:3]

def get_wall_posts(user_id, access_token):
    params = {
        'access_token': access_token,
        'owner_id': user_id,
        'count': 100,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/wall.get', params=params).json()
    
    if 'response' in response and isinstance(response['response'], dict) and 'items' in response['response']:
        return response['response']['items']
    else:
        return []

def count_likes_and_comments(user_id, access_token):
    wall_posts = get_wall_posts(user_id, access_token)
    likes_count = 0
    comments_count = 0
    
    for post in wall_posts:
        likes_count += post['likes']['count']
        comments_count += post['comments']['count']
    
    return likes_count, comments_count

active_friends = get_active_friends(access_token)
print('Количество друзей:', len(active_friends))
print('Топ-3 самых активных друзей по лайкам, комментариям и репостам:')
top_active_friends = get_top_active_friends(access_token)
for friend in top_active_friends:
    friend_info = get_user_info(friend[0], access_token)
    print('User ID:', friend[0])
    print('Total Count:', friend[1])
    likes_count, comments_count = count_likes_and_comments(friend[0], access_token)
    print('Количество лайков на странице:', likes_count)
    print('Количество комментариев на странице:', comments_count)
    print('---')

likes_count, comments_count = count_likes_and_comments(get_user_id(access_token), access_token)
print('Количество лайков на вашей странице:', likes_count)
print('Количество комментариев на вашей странице:', comments_count)
