#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import requests
import warnings
import driver
import headers

warnings.filterwarnings("ignore")

m = driver.Mongo()
m.connect()
tm_headers = headers.tm_headers
count = 0;
usedid_tm = {}
usedid_jd = {}
usedid_ymx = {}
usedid_jmyp = {}


def tm_urls(query, page=0):
    global count
    global usedid_tm
    s = str(60 * page)
    qStr = "https://list.tmall.com/search_product.htm?q=" + query + "&s=" + s
    r = requests.get(qStr, headers=tm_headers)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find_all('a')
    for rrr in result:
        url = rrr.get("href")
        if not url:
            continue
        if "?id" in url:
            id = url[31:url.index("&")]
            if id in usedid_tm:
                continue
            usedid_tm[id] = 1
            count = count + 1
            post = {"website": "tm", "id": id, "type": query}
            m.insert("urls", post)
            print(count, " : ", post)


def jd_urls(query, page=0):
    global count
    global usedid_jd
    s = str(page)
    qStr = "http://search.jd.com/Search?keyword=" + query + "&enc=utf-8&page=" + s
    r = requests.get(qStr, headers=tm_headers)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find_all('a')
    for rrr in result:
        url = rrr.get("href")
        if "item" in url:
            # print (url)
            id = url[14:url.index('.h')]
            if id in usedid_jd:
                continue
            usedid_jd[id] = 1
            count = count + 1
            post = {"website": "jd", "id": id, "type": query}
            m.insert("urls_jd", post)
            print(count, " : ", post)


def ymx_urls(query, page=0):
    global count
    global usedid_ymx
    s = str(page + 1)
    qStr = "https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=" + query + "&page=" + s
    r = requests.get(qStr, headers=tm_headers)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find_all('a')
    for rrr in result:
        url = rrr.get("href")
        if not url:
            continue
        if "qid" in url and "https:" in url:
            if url in usedid_ymx:
                continue
            usedid_ymx[url] = 1
            count = count + 1
            post = {"website": "ymx", "url": url, "type": query}
            m.insert("urls_ymx", post)
            print(count, " : ", post)


def jmyp_urls(query, page=0):
    global count
    global usedid_jmyp
    s = str(page + 1)
    qStr = "http://search.jumei.com/?filter=0-0-" + s + "&search=%E5%8F%A3%E7%BA%A2"
    r = requests.get(qStr, headers=tm_headers)
    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find_all('a')
    for rrr in result:
        url = rrr.get("href")
        if not url:
            continue
        if "item" in url:
            id = url[url.index('m/') + 2:url.index('.h')]
            if id in usedid_jmyp:
                continue
            usedid_jmyp[id] = 1
            count = count + 1
            post = {"website": "jmyp", "id": id, "type": query}
            m.insert("urls_jmyp", post)
            print(count, " : ", post)
