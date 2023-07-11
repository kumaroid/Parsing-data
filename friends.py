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
