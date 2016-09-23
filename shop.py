#!/usr/bin/env python
# encoding: utf-8
import driver
import json

class Product(object):
    def __init__(self, name, price, url,picurl):
        self.name = name;
        self.price = price;
        self.url = url;
        self.picurl = picurl;
        self.describe = ""

class sqlProduct(object):
    def __init__(self,mongo,collection):
        self.mongo = mongo
        self.col = collection

    def insert(self,product):
         temp = {"name":product.name,"price":product.price,"picurl":product.picurl,"url":product.url,"describe":product.describe}
         post = json.dump(temp)
         self.mongo.insert(self.col,post)

