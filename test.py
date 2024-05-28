import tweepy
import pandas as pd
import datetime

consumer_key = "fSAXyRrt7GITUSSo4IlqhgYtI" #Your API/Consumer key 
consumer_secret = "iKshVuyGrBmlSNPkwFP0Svnhowbj9YE1NUOKkSm6sj1gyxJyv9" #Your API/Consumer Secret Key
access_token = "806765394199330817-yXWqaTwmBhBdUJvjgOvg0h9UsM9HG5D"    #Your Access token key
access_token_secret = "uw0pzAbA5vujhOdatP2aWklpakM5bDEQqqDsQUa2aQPy6" #Your Access token Secret key


# Аутентификация
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Функция для получения твитов
def get_tweets(username, since_date):
    tweets_data = []
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended").items():
        if tweet.created_at >= since_date:
            tweet_info = {
                'id': tweet.id,
                'created_at': tweet.created_at,
                'full_text': tweet.full_text,
                'retweet_count': tweet.retweet_count,
                'favorite_count': tweet.favorite_count,
                'reply_count': tweet.reply_count if hasattr(tweet, 'reply_count') else None,
                'quote_count': tweet.quote_count if hasattr(tweet, 'quote_count') else None
            }
            tweets_data.append(tweet_info)
        else:
            break
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
