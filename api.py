import tweepy
import pandas as pd
import base64
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging
import socket
import socks
import os


os.system("cls")



# SOCKS5_PROXY_HOST = "183.64.239.19"
# SOCKS5_PROXY_PORT = 8060

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
# socket.socket = socks.socksocket


# http1 = 'http://175.193.58.170:3128'
# http2 = 'http://72.195.101.99:4145'
# http3 = 'http://200.6.175.10:59341'
# https1 = 'http://175.193.58.170:3128'
# https2 = 'http://72.195.101.99:4145'
# https3 = 'http://200.6.175.10:59341'


# proxies = {
#     'http': http1,
#     'http': http2,
#     'http': http3,
#     'https': https1,
#     'https': https2,
#     'https': https3
# }

# session = requests.Session()

# # session.proxies.update(proxies)
# retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
# adapter = HTTPAdapter(max_retries=retries)
# session.mount("http://", adapter)
# session.mount("https://", adapter)


consumer_key = "fSAXyRrt7GITUSSo4IlqhgYtI"
consumer_secret_key = "iKshVuyGrBmlSNPkwFP0Svnhowbj9YE1NUOKkSm6sj1gyxJyv9"
access_token = "806765394199330817-yXWqaTwmBhBdUJvjgOvg0h9UsM9HG5D"
access_secret_token = "uw0pzAbA5vujhOdatP2aWklpakM5bDEQqqDsQUa2aQPy6"
bearer_token = "AAAAAAAAAAAAAAAAAAAAADSMtwEAAAAA7LdLaxVnZdL2uHR7jd%2F%2B7wYsYxs%3DTOoFNPqHcRSBmBa5TY6NmhJhFtW1PnyK9Zbza4W7uHxyDWutBi"
# encoded_consumer_key = consumer_key.encode()
# encoded_consumer_secret_key = consumer_secret_key.encode()
# encoded_access_token = access_token.encode()
# encoded_access_secret_token = access_secret_token.encode()
# encoded_bearer_token= bearer_token.encode()

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret_key,
    access_token, access_secret_token
)

api = tweepy.API(auth, wait_on_rate_limit=True)
search_query = "'ref''world cup' -filter:retweets AND -filter:replies AND -filter:links'"
n_of_tweets = 100

try:
    logging.info("Starting to fetch tweets")
    tweets = api.search_tweets(q=search_query, lang="en", count=n_of_tweets, tweet_mode="extended")
    logging.info("Fetched tweets success")
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]
    columns = ["User", "Date created", "Number of likes", "Source of tweet", "Tweet"]
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
    logging.info("Tweets parsed to DataFrame")
    print(tweets_df)
except BaseException as e:
    logging.error(f"Failed to fetch tweets {e}")
# finally:
#     session.close()
#     logging.info("Close the HHTP session")