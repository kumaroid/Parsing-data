import requests
#from config import access_token
#from config import user_id
from bs4 import BeautifulSoup
import datetime
import time

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

def get_active_users(access_token):
    user_id = get_user_id(access_token)
    params = {
        'access_token': access_token,
        'user_id': user_id,
        'fields': 'followers_count', # изменяем параметр на fields=followers_count для получения информации о подписчиках
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/users.getFollowers', params=params)
    active_users = response.json()['response']['items']
    return active_users

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




def get_top_active_users(access_token):
    user_ids = get_active_users(access_token)
    top_active_users = []
    
    for user_id in user_ids:
        user_info = get_user_info(user_id, access_token)
        
        if user_info is not None:
            counters = user_info.get('counters', {})
            total_count = counters.get('likes', 0) + counters.get('comments', 0) + counters.get('reposts', 0)
            top_active_users.append((user_id, total_count))
    
    top_active_users.sort(key=lambda x: x[1], reverse=True)
    return top_active_users[:3]

active_users = get_active_users(access_token)
print('Количество подписчиков:', len(active_users))
print('Топ-3 самых активных пользователей по лайкам, комментариям и репостам:')
top_active_users = get_top_active_users(access_token)
for user in top_active_users:
    print('User ID:', user[0])
    print('Total Count:', user[1])
    # print('Likes:', user['likes_count'])
    # print('Comments:', user['comments_count'])
    # print('Reposts:', user['reposts_count'])
    print('---')
