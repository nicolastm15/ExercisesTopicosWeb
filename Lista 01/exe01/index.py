import tweepy
import configparser

config = configparser.ConfigParser()
config.read("./credentials/config.txt")
consumer_key = config.get("TwitterAPI", "consumer_key")
consumer_secret = config.get("TwitterAPI", "consumer_secret")


try:
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   api = tweepy.API(auth)
   for tweet in tweepy.Cursor(api.search, q='Hello World').items(10):
      print(tweet.text)
except tweepy.TweepError:
   print('Problema na conexão com a API')

