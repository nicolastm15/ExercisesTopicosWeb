from connection import connectToTwitterAPI
import tweepy

try:
   api = connectToTwitterAPI()
   tweetsList = tweepy.Cursor(api.search, q = "qualquer texto").items(10)
   for tweet in tweetsList:
      print(tweet.text)
except tweepy.TweepError:
   print('Problema na conexão com a API')

