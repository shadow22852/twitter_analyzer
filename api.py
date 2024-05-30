# import tweepy
# import pandas as pd
# import base64
# # import requests
# # from requests.adapters import HTTPAdapter
# # from requests.packages.urllib3.util.retry import Retry
# import logging
# # import socket
# # import socks
# import os


# os.system("cls")



# # SOCKS5_PROXY_HOST = "183.64.239.19"
# # SOCKS5_PROXY_PORT = 8060

# # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
# # socket.socket = socks.socksocket


# # http1 = 'http://175.193.58.170:3128'
# # http2 = 'http://72.195.101.99:4145'
# # http3 = 'http://200.6.175.10:59341'
# # https1 = 'http://175.193.58.170:3128'
# # https2 = 'http://72.195.101.99:4145'
# # https3 = 'http://200.6.175.10:59341'


# # proxies = {
# #     'http': http1,
# #     'http': http2,
# #     'http': http3,
# #     'https': https1,
# #     'https': https2,
# #     'https': https3
# # }

# # session = requests.Session()

# # # session.proxies.update(proxies)
# # retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
# # adapter = HTTPAdapter(max_retries=retries)
# # session.mount("http://", adapter)
# # session.mount("https://", adapter)


# consumer_key = "fSAXyRrt7GITUSSo4IlqhgYtI"
# consumer_secret_key = "iKshVuyGrBmlSNPkwFP0Svnhowbj9YE1NUOKkSm6sj1gyxJyv9"
# access_token = "806765394199330817-yXWqaTwmBhBdUJvjgOvg0h9UsM9HG5D"
# access_secret_token = "uw0pzAbA5vujhOdatP2aWklpakM5bDEQqqDsQUa2aQPy6"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAADSMtwEAAAAA7LdLaxVnZdL2uHR7jd%2F%2B7wYsYxs%3DTOoFNPqHcRSBmBa5TY6NmhJhFtW1PnyK9Zbza4W7uHxyDWutBi"
# # encoded_consumer_key = consumer_key.encode()
# # encoded_consumer_secret_key = consumer_secret_key.encode()
# # encoded_access_token = access_token.encode()
# # encoded_access_secret_token = access_secret_token.encode()
# # encoded_bearer_token= bearer_token.encode()

# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret_key,
#     access_token, access_secret_token
# )

# api = tweepy.API(auth, wait_on_rate_limit=True)
# search_query = "'ref''world cup' -filter:retweets AND -filter:replies AND -filter:links'"
# n_of_tweets = 100

# try:
#     logging.info("Starting to fetch tweets")
#     tweets = api.search_tweets(q=search_query, lang="en", count=n_of_tweets, tweet_mode="extended")
#     logging.info("Fetched tweets success")
#     attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]
#     columns = ["User", "Date created", "Number of likes", "Source of tweet", "Tweet"]
#     tweets_df = pd.DataFrame(attributes_container, columns=columns)
#     logging.info("Tweets parsed to DataFrame")
#     print(tweets_df)
# except BaseException as e:
#     logging.error(f"Failed to fetch tweets {e}")
# # finally:
# #     session.close()
# #     logging.info("Close the HHTP session")

# import tweepy
# import time
# import os

# os.system("cls")
# # Ваши ключи API
# bearer_token = "AAAAAAAAAAAAAAAAAAAAADSMtwEAAAAA7LdLaxVnZdL2uHR7jd%2F%2B7wYsYxs%3DTOoFNPqHcRSBmBa5TY6NmhJhFtW1PnyK9Zbza4W7uHxyDWutBi"

# # Ваши ключи API

# # Настройка клиента
# client = tweepy.Client(bearer_token=bearer_token)

# # Список имен пользователей (screen names)
# usernames = ['JoeBiden', 'ElonMusk']  # Замените на нужные вам имена пользователей

# def get_user_info(usernames):
#     user_data = []
#     for username in usernames:
#         try:
#             # Ограничения: не более 300 запросов за 15 минут
#             if len(user_data) % 300 == 0 and len(user_data) > 0:
#                 print("Достигнут лимит запросов. Ожидание 15 минут...")
#                 time.sleep(15 * 60)  # Ожидание 15 минут
            
#             user = client.get_user(username=username)
#             user_data.append({
#                 'Username': username,
#                 'Name': user.data.name,
#                 'Followers': user.data.public_metrics['followers_count'],
#                 'Following': user.data.public_metrics['following_count'],
#                 'Tweets': user.data.public_metrics['tweet_count'],
#                 'Account Creation Date': user.data.created_at
#             })
#         except tweepy.TweepyException as e:
#             print(f"Failed to get data for {username}: {e}")
#     return user_data

# # Получение данных
# user_info = get_user_info(usernames)

# # Преобразование в DataFrame
# import pandas as pd
# df = pd.DataFrame(user_info)
# print(df)



# import tweepy
# import json
# import os
# import datetime
# import pandas as pd
# import time
# # import logging

# os.system("cls")
# print("Start progamm")
# def get_tweets(username):
#     tweets_data = []
#     try:
#         user = client.get_user(username=username)
#         user_id = user.data.id
#         query = f"from:{username} -is:retweet"
#         since_date = datetime.datetime.now() - datetime.timedelta(days=365)
#         end_time = since_date.isoformat("T") + "Z"

#         paginator = tweepy.Paginator(client.search_all_tweets, query=query, tweet_fields=["created_at", "public_metrics"],
#                                     start_time=end_time, max_results=100)
        
#         for tweet in paginator.flatten(limit=100):
#             tweet_info = {
#                 'id': tweet.id,
#                 'created_at': tweet.created_at,
#                 'full_text': tweet.text,
#                 'retweet_count': tweet.public_metrics['retweet_count'],
#                 'reply_count': tweet.public_metrics['reply_count'],
#                 'like_count': tweet.public_metrics['like_count'],
#                 'quote_count': tweet.public_metrics['quote_count']
#             }
#             tweets_data.append(tweet_info)
#     except tweepy.TweepyException as e:
#         print(f"An error {e}")
#     return tweets_data

# def get_bearer_from_json():
#     bearer_list = []
#     with open ("keys.json") as f:
#         data = json.load(f)
#         keys = list(data.keys())
#     for k in keys:
#         if "bearer" in k:
#             bearer_list.append(data[k])
#     return bearer_list

# bearer_list = get_bearer_from_json()

# for x in range(len(bearer_list)):
#     bearer_token = bearer_list[x]
#     print(f"Number of bearer_token: {x},\n value of bearer_token: {bearer_token}")
#     client = tweepy.Client(bearer_token=bearer_token)
#     username = "JoeBiden"
#     tweets_data = get_tweets(username)
#     df = pd.DataFrame(tweets_data)
#     print(df)
#     time.sleep(10)


import tweepy
import time
import json
import os

os.system("cls")
print("~~~starting~~~")

def get_bearer_from_json():
    bearer_list = []
    with open("keys.json") as f:
        data = json.load(f)
        keys = list(data.keys())
    for k in keys:
        if "bearer" in k:
            bearer_list.append(data[k])
    return bearer_list


def check_bearer_tokens(bearer_list):
    valid_tokens = []
    for bearer_token in bearer_list:
        try:
            client = tweepy.Client(bearer_token=bearer_token)
            # Попробуем получить информацию о текущем пользователе
            client.get_me()
            print(f"Bearer token {bearer_token} is valid.")
            valid_tokens.append(bearer_token)
        except tweepy.TweepyException as e:
            print(f"Bearer token {bearer_token} is invalid: {e}")
        time.sleep(1)  # Задержка для предотвращения превышения лимита запросов
    return valid_tokens

bearer_list = get_bearer_from_json()
valid_tokens = check_bearer_tokens(bearer_list)

if valid_tokens:
    print("Valid tokens found:")
    for token in valid_tokens:
        print(token)
else:
    print("No valid tokens found.")