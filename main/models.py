from pymongo import MongoClient

key = 'mongodb+srv://h_rl:vovochka2004@cluster0.udvcs.mongodb.net/votings'
client = MongoClient(key)

db = client.votings
db_users = db.users
db_posts = db.posts

users = []
posts = []


class DbObj:
    list = []

    def save(self):
        self.list.insert_one(self.__dict__)


def classify(name, dictionary):
    obj = name
    for key, value in dictionary.items():
        setattr(obj, key, value)
    return obj

