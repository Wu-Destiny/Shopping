# encoding: utf-8
import pymongo
import logging
from pymongo import MongoClient

logger = logging.getLogger('main.mod')

class Mongo(object):
    def connect(self):
        # client = MongoClient()
        self.client = MongoClient("localhost", 12306)
        self.db = self.client['shopping']
        logger.info("db connect")

    def insert(self,collection,post,flag = 0):
        if flag == 0:
            post_id  = self.db[collection].insert_one(post)
        # flag = 0 shows that there is only one insert post
        # flag = 1 shows that there are posts to be insert
        pass

    def update(self,collection,post):
        pass

    def findall(self,collection,query=""):
        if query=="":
            return self.db[collection].find()

    def findone(self,collection,query):
        pass

    def display(self,collection):
          i = 0
          for f in self.db[collection].find():
            i = i + 1
            print (i,":",f)
          print ("--------",i,"--------")

    def delete(self,collection,query):
        pass
if __name__ == '__main__':
    m = Mongo()
    m.connect()
    # m.display("urls_ymx")
    # m.display("urls")
    # m.display("urls_jd")
    m.display("pro_ymx")