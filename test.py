import tweepy
import pandas as pd
import datetime
import os
import json

with open ("keys.json") as f:
    data = json.load(f)
    keys = list(data.keys())

os.system("cls")
def get_bearer_from_json():
    bearer_list = []
    with open ("keys.json") as file:
        data = json.load(file)
        keys = list(data.keys())
    for k in keys:
        if "bearer" in k:
            bearer_list.append(data[k])
    return bearer_list

bearer_list = get_bearer_from_json()

for x in range(len(bearer_list)):
    bearer_token = str(bearer_list[x])

    # Аутентификация
    client = tweepy.Client(bearer_token=bearer_token)

    # Функция для получения твитов
    def get_tweets(username, since_date):
        tweets_data = []
        user = client.get_user(username=username)
        user_id = user.data.id

        query = f'from:{username} -is:retweet'
        end_time = since_date.isoformat("T") + "Z"
        
        paginator = tweepy.Paginator(client.search_all_tweets, query=query, tweet_fields=['created_at', 'public_metrics'], 
                                    start_time=end_time, max_results=100)
        
        for tweet in paginator.flatten(limit=1000):  # ограничение по количеству твитов
            tweet_info = {
                'id': tweet.id,
                'created_at': tweet.created_at,
                'full_text': tweet.text,
                'retweet_count': tweet.public_metrics['retweet_count'],
                'reply_count': tweet.public_metrics['reply_count'],
                'like_count': tweet.public_metrics['like_count'],
                'quote_count': tweet.public_metrics['quote_count']
            }
            tweets_data.append(tweet_info)
        
        return tweets_data

    # Основной код
    username = 'POTUS'  # Официальный аккаунт Джо Байдена
    since_date = datetime.datetime.now() - datetime.timedelta(days=365)  # За последний год

    tweets_data = get_tweets(username, since_date)

    # Создание DataFrame
    df = pd.DataFrame(tweets_data)
    print(df)
    # Сохранение в CSV файл
    df.to_csv(f'{username}_tweets_stats.csv', index=False)

    print(f"Статистика твитов сохранена в {username}_tweets_stats.csv")


