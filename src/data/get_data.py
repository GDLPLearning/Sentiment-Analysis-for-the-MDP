# get_data.py
""" """
import tweepy
import keys
import bcrypt  # Good password hashing for your software and your servers

# Creating and Configuring an OAuthHandler to Authenticate with Twitter
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Encrypt the keys
consumer_key = bcrypt.hashpw(consumer_key.encode(), bcrypt.gensalt())
consumer_secret = bcrypt.hashpw(consumer_secret.encode(), bcrypt.gensalt())
access_token = bcrypt.hashpw(access_token.encode(), bcrypt.gensalt())
access_token_secret = bcrypt.hashpw(access_token_secret.encode(), bcrypt.gensalt())

# Creating an API Object
api = tweepy.API(auth, wait_on_rate_limit=True)

# print(consumer_key)
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*60}')