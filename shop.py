#!/usr/bin/env python
# encoding: utf-8
import driver
import json


class Product(object):
    def __init__(self, name, price, url, picurls, detail, id, website, type, time):
        self.name = name
        self.price = price
        self.url = url
        self.picurls = picurls
        self.detail = detail
        self.id = id
        self.website = website
        self.type = type
        self.time = time


class sqlProduct(object):
    def __init__(self, mongo, collection):
        self.mongo = mongo
        self.col = collection

    def insert(self, product):
        temp = {"name": product.name, "price": product.price, "picurls": product.picurls, "url": product.url,
                "detail": product.detail,
                "id": product.id, "website": product.website, "type": product.type, "time": product.time}
        self.mongo.insert(self.col, temp)
