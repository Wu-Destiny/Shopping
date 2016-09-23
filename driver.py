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

    def findone(self,collection,query):
        pass

    def findall(self,collection,query):
        pass

    def display(self,collection):
          i = 0
          for f in self.db[collection].find():
            i = i + 1
            print (i,":",f)

    def delete(self,collection,query):
        pass

m = Mongo()
m.connect()
m.display("urls")