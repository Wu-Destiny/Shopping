#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import requests
import warnings
import driver
warnings.filterwarnings("ignore")

m = driver.Mongo()
m.connect()

tm_headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'accept-encoding':'gzip, deflate, sdch, br',
'accept-language':'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
'cookie':'cna=oRegD+tVDV0CAdOiUXLIKgxx; lzstat_uv=35195752721611602248|3576861; _med=dw:1920&dh:1080&pw:1920&ph:1080&ist:0; x=__ll%3D-1%26_ato%3D0; swfstore=65680; _m_h5_tk=ec5cdb84003d99e2c80b91722428fa4a_1474640732495; _m_h5_tk_enc=d72c5a43b6bce74f33323c015f825cb6; sm4=520100; _dqc_u_l=%E5%8D%97%E4%BA%AC%E5%B8%82; ck1=; tk_trace=1; _tb_token_=bhfEcgD4Lgtm; hng=CN%7Czh-cn%7CCNY; uc1=cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false; uc3=nk2=rXviG8X%2F&id2=UonYs9iYjZG6Ng%3D%3D&vt3=F8dAS1HqaietjNfctRw%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; uss=W5tV8GoeLv7eIGCI9qimcHlHxaojVDWF8LSVW38P%2BgEPFzY5VOrTyR8kTw%3D%3D; lgc=%5Cu5434%5Cu4E2D%5Cu6BC5; tracknick=%5Cu5434%5Cu4E2D%5Cu6BC5; cookie2=2bf89c239c4c411686c46d0848eb56c1; cookie1=W5tWYU%2B%2F55G4GhImAxbbeoI17z0cjW%2F%2B12O1sWlpCkw%3D; unb=1832326719; skt=4b04730119785572; t=959a473bdf95f3325fbed00200e3f19c; _l_g_=Ug%3D%3D; _nk_=%5Cu5434%5Cu4E2D%5Cu6BC5; cookie17=UonYs9iYjZG6Ng%3D%3D; login=true; cq=ccp%3D0; tt=sec.taobao.com; pnm_cku822=229UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5OcktxSHNLcURwT3pFfSs%3D%7CU2xMHDJ7G2AHYg8hAS8XKQcnCVU0Uj5ZJ11zJXM%3D%7CVGhXd1llXGZfZFxmU2dYbVJqXWBCd09xRHFEfEJ3SnFPe0Z6Q207%7CVWldfS0RMQ05Aj8fIxo6FGVcYVVzTnZKdF5rUXRCbDps%7CVmhIGCUFOBgkES4bOwM4BTsbJxMsETENMAU4GCQRKBAwDDEEOW85%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; res=scroll%3A1828*5603-client%3A1828*941-offset%3A1828*5603-screen%3A1920*1080; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; whl=-1%260%260%260; l=AvT0KKhf/peheewbkYLnCsyDRLhm7Bi3; isg=ArS04xK7XwK0y8tYTLs0TCObhXII9Nh3KsHDfE4VYT_CuVQDd52oB2pzT0ab',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

count = 0;
usedid_tm = {}
def tm_urls(query,page=0):
    global count
    global usedid_tm
    s = str(60*page)
    qStr = "https://list.tmall.com/search_product.htm?q=" + query+"&s="+s
    r = requests.get(qStr,headers=tm_headers)
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
            count = count+1
            post = {"website":"tm","id":id,"type":query}
            m.insert("urls",post)
            print (count," : ",post)


