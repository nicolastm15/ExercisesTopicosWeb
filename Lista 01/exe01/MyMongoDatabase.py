import configparser
import pymongo

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

config = configparser.ConfigParser()
config.read("./credentials/config.ini")
myMongoCreds = {'username': quote_plus(config.get("MongoDB", "username")), 'password': quote_plus(
    config.get("MongoDB", "password"))}
myMongoUrl = 'mongodb+srv://%s:%s@cluster0.sofkp.gcp.mongodb.net' % (
    myMongoCreds['username'], myMongoCreds['password'])


class MyMongoDatabase:
    def __init__(self, dbName):
        myMongoClient = pymongo.MongoClient(myMongoUrl)
        self.db = myMongoClient[dbName]

    def insert(self, collectionName, tweet):
        tweetsCollection = self.db[collectionName]
        tweetsCollection.insert_one(tweet)
