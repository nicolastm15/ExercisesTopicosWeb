import tweepy
import configparser

def connectToTwitterAPI():
   config = configparser.ConfigParser()
   config.read("./credentials/config.ini")
   consumer_key = config.get("TwitterAPI", "consumer_key")
   consumer_secret = config.get("TwitterAPI", "consumer_secret")
   auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
   return tweepy.API(auth)
