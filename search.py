#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import requests
import warnings
import shop

warnings.filterwarnings("ignore")

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': 'cna=oRegD+tVDV0CAdOiUXLIKgxx; lzstat_uv=35195752721611602248|3576861; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; x=__ll%3D-1%26_ato%3D0; swfstore=65680; _m_h5_tk=ec5cdb84003d99e2c80b91722428fa4a_1474640732495; _m_h5_tk_enc=d72c5a43b6bce74f33323c015f825cb6; sm4=520100; _dqc_u_l=%E5%8D%97%E4%BA%AC%E5%B8%82; ck1=; _tb_token_=bhfEcgD4Lgtm; uc3=nk2=rXviG8X%2F&id2=UonYs9iYjZG6Ng%3D%3D&vt3=F8dAS1HqbIufy6%2BnL38%3D&lg2=UtASsssmOIJ0bQ%3D%3D; uss=W5tV8GoeLv7eIGCI9qimcHlHxaojVDWF8LSVW38P%2BgEPFzY5VOrTyR8kTw%3D%3D; lgc=%5Cu5434%5Cu4E2D%5Cu6BC5; tracknick=%5Cu5434%5Cu4E2D%5Cu6BC5; skt=d842e66f66a7fc1d; hng=CN%7Czh-cn%7CCNY; cookie2=2bf89c239c4c411686c46d0848eb56c1; t=959a473bdf95f3325fbed00200e3f19c; whl=-1%260%260%260; tk_trace=1; pnm_cku822=014UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5OcktxSHNLc09zTnRAfyk%3D%7CU2xMHDJ7G2AHYg8hAS8XKQcnCVU0Uj5ZJ11zJXM%3D%7CVGhXd1llXGZfZFxkWGRZY1doX2JAe0V9QX1FcEV9Q3lAdUhxRWs9%7CVWldfS0SMg46AyMfIwMtCHoTK3tGECBaOQYofig%3D%7CVmhIGCUFOBgkES4bOwM2DzcXKx8gHT0BPAk0FCgdJBw8AD0INWM1%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; res=scroll%3A1828*5845-client%3A1828*941-offset%3A1828*5845-screen%3A1920*1080; cq=ccp%3D1; l=Aj09zpX31-xAJvVAwPU-oUBhzZM32nEs; isg=AnNzJgawIP_C6-w9p_57IehmAnfJ8wdq8UzkWSUQzxLJJJPGrXiXutG-qOMw; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}


class Search(object):
    def __init__(self):
        self.body = []
        self.list = []

    def search(self, query):
        return "please define the search function."

    def getDescribe(self, url):
        return ""

    def printSearch(self, query):
        if (len(self.list) == 0):
            self.search(query)
        list = self.list
        for l in list:
            print(l.name, l.price, l.url, l.picurl)


class tmSearch(Search):
    def __init__(self):
        self.body = []
        self.list = []

    def getDescribe(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        describe = soup.find(id="J_AttrUL").text
        return describe

    def search(self, query):
        qStr = "https://list.tmall.com/search_product.htm?q=" + query
        r = requests.get(qStr, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        result = soup.find_all('div', class_="product-iWrap")
        for rrr in result:
            img = rrr.find("img").get("src")
            if not img:
                img = img = rrr.find("img").get("data-ks-lazyload")
            name = rrr.find_all("a")[1].get("title")
            price = rrr.find("p", class_="productPrice")
            if not price:
                continue
            price = price.find("em").get("title")
            url = "https:" + rrr.find('a').get("href")
            pro = shop.Product(name, price, url, img)
            self.list.append(pro)
        return self.list

    def describe(self):
        for l in self.list:
            l.describe = self.getDescribe(l.url)
            print(l.describe)


if __name__ == '__main__':
    tm = tmSearch()
    tm.printSearch("小米手机")
    # tm.describe()
# r = requests.get("")
# soup = BeautifulSoup(r.text,"html.parser")

# print soup.head
