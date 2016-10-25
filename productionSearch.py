from bs4 import BeautifulSoup
import requests
import warnings
import driver
import headers
import time
import shop
import simplejson as json
import logging
import logging.config
import urllib.parse

logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
logger = logging.getLogger('main')
warnings.filterwarnings("ignore")

m = driver.Mongo()
m.connect()

count = 0


def proTm():
    list = m.findall("urls")
    for l in list:
        try:
            global count
            count = count + 1
            if count < 589:
                continue
            id = l['id'];
            type = l['type'];
            website = l['website'];
            qStr = "https://detail.tmall.com/item.htm?id=" + id
            r = requests.get(qStr, headers=headers.tm_headers)
            price = r.text.find("defaultItemPrice")
            i = int(price)
            while 1:
                if r.text[i] == ',':
                    break
                i = i + 1
            soup = BeautifulSoup(r.text, "html.parser")
            img = soup.find('div', class_="tb-booth").find('img')
            name = img.get('alt')
            url = qStr
            price = r.text[int(price) + 19:i - 1]
            picurl = img.get('src')
            detail = soup.find(id='J_AttrUL').text
            now = time.strftime("%Y-%m-%d", time.localtime())
            # print(name, price,url, picurl, detail, id, type, website, now)
            p = shop.Product(name, price, url, picurl, detail, id, website, type, now)
            sql = shop.sqlProduct(m, "pro_tm")
            sql.insert(p)
            print(count, name, id, website)
        except Exception:
            print(count, price)
            logger.info(Exception)


def proJd():
    list = m.findall("urls_jd")
    for l in list:
        try:
            global count
            count = count + 1
            if count < 679:
                continue
            id = l['id']
            type = l['type']
            website = l['website']
            qStr = "https://item.jd.com/" + id + ".html"
            r = requests.get(qStr, headers=headers.tm_headers)
            soup = BeautifulSoup(r.text, "html.parser")
            img = soup.find(id="spec-n1").find('img')
            name = img.get('alt')
            picurl = img.get('src')
            url = qStr
            nameEnd = len(name)
            if name.rfind('#') != -1:
                name = name[:name.rfind('#')]
            if name.rfind('(') != -1 or name.rfind('（') != -1:
                nameEnd = (max(name.rfind('('), name.rfind('（')))
            name = name[:nameEnd]
            detail = soup.find(id='parameter2').text
            now = time.strftime("%Y-%m-%d", time.localtime())
            price = 0
            qPrice = "http://search.jd.com/Search?keyword=" + name + "&enc=utf-8"
            r = requests.get(qPrice, headers=headers.tm_headers)
            soup = BeautifulSoup(r.text, "html.parser")
            price = soup.find('div', class_="p-price").find('strong', class_="J_" + id).get('data-price')
            # print(name, price, url, picurl, detail, id, type, website, now)
            p = shop.Product(name, price, url, picurl, detail, id, website, type, now)
            sql = shop.sqlProduct(m, "pro_jd")
            sql.insert(p)
            print(count, name, id, website, price)
        except Exception:
            print(count, qPrice)
            logger.info(Exception)


hashYmx = {}


def proYmx():
    list = m.findall("urls_ymx")
    for l in list:
        try:
            url = l['url']
            name = url.find('n/')
            name = url[name + 2:]
            end = name.find('/')
            name = name[:end]
            name = urllib.parse.unquote(name)
            global count
            if name in hashYmx:
                continue
            hashYmx[name] = 1
            count = count + 1
            if count < 0:
                continue
            type = l['type']
            website = l['website']
            id = ""
            if url.find("page") != -1:
                continue
            r = requests.get(url, headers=headers.tm_headers)
            soup = BeautifulSoup(r.text, "html.parser")
            picurl = soup.find(id='imgTagWrapperId').find('img').get('src')
            price = soup.find('div', class_='priceText').text.replace('￥', '')
            detail = soup.find('div', class_='content').text
            now = time.strftime("%Y-%m-%d", time.localtime())
            # print(name, price, url, detail, id, type, website, now, picurl)
            p = shop.Product(name, price, url, picurl, detail, id, website, type, now)
            sql = shop.sqlProduct(m, "pro_ymx")
            sql.insert(p)
            print(count, name, id, website, price)
        except Exception:
            print(url)
            logger.info(Exception)


def proJmyp():
    list = m.findall("urls_jmyp")
    for l in list:
        try:
            global count
            count = count + 1
            if count < 1:
                continue
            id = l['id'];
            type = l['type'];
            website = l['website'];
            if id.find('h') == -1:
                continue
            print(count, id, type, website)
            qStr = "http://item.jumei.com/" + id + ".html"
            r = requests.get(qStr, headers=headers.tm_headers)
            # print(qStr)
            print(r.text)
            # price = r.text.find("defaultItemPrice")
            # i = int(price)
            # while 1:
            #     if r.text[i] == ',':
            #         break
            #     i = i + 1
            # soup = BeautifulSoup(r.text, "html.parser")
            # img = soup.find('div', class_="tb-booth").find('img')
            # name = img.get('alt')
            # url = qStr
            # price = r.text[int(price) + 19:i - 1]
            # picurl = img.get('src')
            # detail = soup.find(id='J_AttrUL').text
            # now = time.strftime("%Y-%m-%d", time.localtime())
            # # print(name, price,url, picurl, detail, id, type, website, now)
            # p = shop.Product(name, price, url, picurl, detail, id, website, type, now)
            # sql = shop.sqlProduct(m, "pro_jmyp")
            # sql.insert(p)
            # print(count, name, id, website)
            break
        except Exception:
            print(count)
            logger.info(Exception)
